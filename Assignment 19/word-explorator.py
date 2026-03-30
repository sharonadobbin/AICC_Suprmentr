# Word Importance Explorer using TF-IDF

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import os

# Folder path
folder = "sample_docs"

# File names with path
file_names = [os.path.join(folder, f"doc{i}.txt") for i in range(1, 6)]

# Initialize documents list
documents = []

# Load documents
for file in file_names:
    with open(file, "r", encoding="utf-8") as f:
        documents.append(f.read())

# Apply TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)

# Get feature names (words)
feature_names = vectorizer.get_feature_names_out()

# Extract top keywords per document
top_n = 5

for doc_index, doc_vector in enumerate(tfidf_matrix):
    print(f"\nDocument {doc_index + 1} Top Keywords:\n")

    scores = doc_vector.toarray().flatten()
    top_indices = scores.argsort()[-top_n:][::-1]

    for idx in top_indices:
        word = feature_names[idx]
        score = scores[idx]

        explanation = (
            f"'{word}' is important because it appears frequently in this document "
            f"but is relatively rare in other documents (TF-IDF score: {score:.4f})."
        )

        print(f"Keyword: {word}")
        print(f"Score: {score:.4f}")
        print(f"Explanation: {explanation}\n")