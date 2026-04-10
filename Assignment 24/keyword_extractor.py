import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string

# Download required resources (only runs first time)
nltk.download('punkt')
nltk.download('stopwords')

def extract_keywords(text, num_keywords=10):
    # Convert text to lowercase
    text = text.lower()
    
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Load English stopwords
    stop_words = set(stopwords.words('english'))
    
    # Remove stopwords, punctuation, and non-alphanumeric words
    filtered_words = [
        word for word in words 
        if word not in stop_words 
        and word not in string.punctuation 
        and word.isalnum()
    ]
    
    # Count frequency of each word
    word_freq = Counter(filtered_words)
    
    # Get the most common keywords
    keywords = word_freq.most_common(num_keywords)
    
    return keywords

# Main program
if __name__ == "__main__":
    print("=== Keyword Extractor ===")
    text = input("Enter your text: ")
    
    keywords = extract_keywords(text)
    
    print("\nTop Keywords:")
    for word, freq in keywords:
        print(f"{word} (frequency: {freq})")