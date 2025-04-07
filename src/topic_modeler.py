from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF
import pandas as pd

def train_topic_model(texts, n_topics=10, n_top_words=10):
    tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
    tf = tf_vectorizer.fit_transform(texts)
    nmf = NMF(n_components=n_topics, random_state=42).fit(tf)
    return nmf, tf_vectorizer

def get_topic_words(model, feature_names, n_top_words):
    topics = []
    for topic_idx, topic in enumerate(model.components_):
        topics.append(" ".join([feature_names[i] 
                              for i in topic.argsort()[:-n_top_words-1:-1]]))
    return topics

def assign_topics(model, tf_matrix, df):
    topic_dist = model.transform(tf_matrix)
    df['dominant_topic'] = topic_dist.argmax(axis=1)
    return df