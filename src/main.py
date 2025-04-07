from youtube_api import get_video_id, get_video_title, get_transcript
from transcript_processor import save_transcript, load_transcript
from topic_modeler import train_topic_model, get_topic_words, assign_topics
from chapter_generator import detect_chapter_breaks, generate_chapter_names
import yaml

def main():
    # Load config
    with open('config/api_keys.yaml') as f:
        config = yaml.safe_load(f)
    
    # Get YouTube data
    url = input("Enter YouTube URL: ")
    video_id = get_video_id(url)
    title = get_video_title(config['youtube_api_key'], video_id)
    transcript = get_transcript(video_id)
    
    # Process transcript
    save_transcript(transcript, title, f"data/raw/{video_id}.csv")
    df = load_transcript(f"data/raw/{video_id}.csv")
    
    # Topic modeling
    nmf, vectorizer = train_topic_model(df['text'])
    df = assign_topics(nmf, vectorizer.transform(df['text']), df)
    
    # Generate chapters
    breaks = detect_chapter_breaks(df)
    topics = get_topic_words(nmf, vectorizer.get_feature_names_out(), 10)
    chapters = generate_chapter_names(df, breaks, topics)
    
    # Save output
    pd.DataFrame(chapters).to_csv(f"outputs/chapters/{video_id}_chapters.csv", index=False)
    print("\nGenerated Chapters:")
    for chap in chapters:
        print(f"{chap['time']} - {chap['name']}")

if __name__ == "__main__":
    main()