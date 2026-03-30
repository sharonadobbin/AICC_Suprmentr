# Movie Review Analyzer using TextBlob

from textblob import TextBlob
import os

# Folder containing reviews
folder = "reviews"

# File names: review1.txt to review5.txt
file_names = [os.path.join(folder, f"review{i}.txt") for i in range(1, 6)]

# Analyze each review
for i, file in enumerate(file_names):
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # Determine sentiment with neutral range
    if -0.1 <= polarity <= 0.1:
        sentiment = "Neutral"
    elif polarity > 0.1:
        sentiment = "Positive"
    else:
        sentiment = "Negative"

    print(f"\nReview {i+1}:")
    print(f"Sentiment: {sentiment}")
    print(f"Polarity Score: {polarity:.3f}")