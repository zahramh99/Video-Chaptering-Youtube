import pandas as pd

def save_transcript(transcript, title, filename):
    transcript_data = [{'start': entry['start'], 'text': entry['text']} 
                      for entry in transcript]
    df = pd.DataFrame(transcript_data)
    df.to_csv(filename, index=False)
    
    # Append title
    with open(filename, 'a') as f:
        f.write(f"\nTitle:,{title}")

def load_transcript(filename):
    df = pd.read_csv(filename)
    df['start'] = pd.to_numeric(df['start'], errors='coerce')
    return df.dropna()