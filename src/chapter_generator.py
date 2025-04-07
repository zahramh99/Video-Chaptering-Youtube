import pandas as pd

def detect_chapter_breaks(df, time_threshold=60):
    breaks = []
    for i in range(1, len(df)):
        if df['dominant_topic'].iloc[i] != df['dominant_topic'].iloc[i-1]:
            breaks.append(df['start'].iloc[i])
    
    # Consolidate breaks
    consolidated = []
    last_break = None
    for bp in breaks:
        if last_break is None or (bp - last_break) >= time_threshold:
            consolidated.append(bp)
            last_break = bp
    return consolidated

def generate_chapter_names(df, break_points, topics):
    chapters = []
    for i, bp in enumerate(break_points):
        chapter_text = df[df['start'] >= bp]['text'].str.cat(sep=' ')
        vectorizer = TfidfVectorizer(stop_words='english', max_features=3)
        tfidf = vectorizer.fit_transform([chapter_text])
        name = " ".join(vectorizer.get_feature_names_out())
        chapters.append({
            'start': bp,
            'time': pd.to_datetime(bp, unit='s').strftime('%H:%M:%S'),
            'name': f"Chapter {i+1}: {name}"
        })
    return chapters