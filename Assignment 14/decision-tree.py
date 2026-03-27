import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# -------------------------------
# 1. Create Dataset
# -------------------------------
data = {
    "Weather": ["Sunny", "Sunny", "Overcast", "Rainy", "Rainy", "Rainy", "Overcast", "Sunny"],
    "Humidity": ["High", "Normal", "High", "High", "Normal", "Normal", "Normal", "High"],
    "Wind": ["Weak", "Strong", "Weak", "Weak", "Weak", "Strong", "Strong", "Weak"],
    "Play": ["No", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "No"]
}

df = pd.DataFrame(data)

# -------------------------------
# 2. Convert text to numbers
# -------------------------------
df_encoded = df.copy()

for col in df_encoded.columns:
    df_encoded[col] = df_encoded[col].astype('category').cat.codes

X = df_encoded.drop("Play", axis=1)
y = df_encoded["Play"]

# -------------------------------
# 3. Train Decision Tree
# -------------------------------
model = DecisionTreeClassifier()
model.fit(X, y)

# -------------------------------
# 4. Visualize Tree
# -------------------------------
plt.figure(figsize=(10,6))
plot_tree(model, 
          feature_names=["Weather", "Humidity", "Wind"], 
          class_names=["No", "Yes"], 
          filled=True)

plt.title("Decision Tree: Should You Play Outside?")
plt.show()

# -------------------------------
# 5. Predict New Case
# -------------------------------
print("\n=== Prediction ===")

weather = input("Enter Weather (Sunny/Overcast/Rainy): ")
humidity = input("Enter Humidity (High/Normal): ")
wind = input("Enter Wind (Weak/Strong): ")

# Convert input same way
mapping = {
    "Weather": {"Sunny":0, "Overcast":1, "Rainy":2},
    "Humidity": {"High":0, "Normal":1},
    "Wind": {"Weak":0, "Strong":1}
}

new_data = [[
    mapping["Weather"][weather],
    mapping["Humidity"][humidity],
    mapping["Wind"][wind]
]]

prediction = model.predict(new_data)

result = "Yes" if prediction[0] == 1 else "No"
print("Should you play outside?", result)