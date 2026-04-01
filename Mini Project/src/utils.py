# This module contains utility functions for the resume and job description matching project, such as extracting top keywords from the text.

from collections import Counter
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words('english'))

CUSTOM_STOPWORDS = {
    "experience", "skills", "knowledge", "job", "work", "intern", "engineer", "learning", "responsibilites", "company", "role",
    "team", "using", "required", "preferred", "strong", "ability", "proven", "track", "record", "successfully", "demonstrated", "excellent", "communication",
}

def get_top_keywords(text, top_n=20):
    words = text.split()

    # Remove stopwords + short words
    filtered_words = [
    word for word in words 
    if word not in STOPWORDS 
    and word not in CUSTOM_STOPWORDS
    and len(word) > 2
    ]

    freq = Counter(filtered_words)

    return [word for word, _ in freq.most_common(top_n)]