import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# -------------------------------
# 1. Create Dataset
# -------------------------------
data = {
    "message": [
        "Win a free lottery now",
        "Hello, how are you?",
        "Exclusive offer just for you",
        "Let's meet tomorrow",
        "Congratulations, you won a prize",
        "Are we still on for dinner?",
        "Get cheap loans instantly",
        "Call me when you are free"
    ],
    "label": ["spam", "ham", "spam", "ham", "spam", "ham", "spam", "ham"]
}

df = pd.DataFrame(data)

print("\n--- Dataset ---")
print(df)


# -------------------------------
# 2. Split Data
# -------------------------------
X = df["message"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# -------------------------------
# 3. Feature Extraction
# -------------------------------
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)


# -------------------------------
# 4. Train Model
# -------------------------------
model = MultinomialNB()
model.fit(X_train_vec, y_train)


# -------------------------------
# 5. Evaluation
# -------------------------------
y_pred = model.predict(X_test_vec)

print("\n--- Model Evaluation ---")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# -------------------------------
# 6. Predict New Message
# -------------------------------
print("\n--- Spam Detection ---")
msg = input("Enter a message: ")

msg_vec = vectorizer.transform([msg])
prediction = model.predict(msg_vec)

print("Prediction:", prediction[0])