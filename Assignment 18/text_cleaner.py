import string

# -------------------------------
# Sample Stopwords List
# -------------------------------
stopwords = {
    "is", "am", "are", "the", "a", "an", "and", "or", "in", "on", "at",
    "to", "for", "of", "with", "this", "that", "it"
}

# -------------------------------
# Text Cleaning Function
# -------------------------------
def clean_text(text):
    # 1. Lowercase
    text = text.lower()

    # 2. Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # 3. Tokenize
    words = text.split()

    # 4. Remove stopwords
    cleaned_words = [word for word in words if word not in stopwords]

    # 5. Join back
    cleaned_text = " ".join(cleaned_words)

    return cleaned_text


# -------------------------------
# Test the Cleaner
# -------------------------------
print("=== TEXT CLEANER ===")

user_input = input("Enter text: ")

result = clean_text(user_input)

print("\nCleaned Text:")
print(result)