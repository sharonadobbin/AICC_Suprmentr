# House Price Predictor using Linear Regression

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# -------------------------------
# 1. Create Dataset
# -------------------------------
data = {
    "Area (sq ft)": [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500],
    "Bedrooms": [2, 2, 3, 3, 4, 4, 5, 5],
    "Age (years)": [10, 8, 6, 5, 4, 3, 2, 1],
    "Price": [2000000, 2500000, 3000000, 3800000, 4500000, 5000000, 5500000, 6200000]
}

df = pd.DataFrame(data)

print("\n--- Dataset ---")
print(df)


# -------------------------------
# 2. Feature & Label Split
# -------------------------------
X = df[["Area (sq ft)", "Bedrooms", "Age (years)"]]
y = df["Price"]


# -------------------------------
# 3. Train Model
# -------------------------------
model = LinearRegression()
model.fit(X, y)


# -------------------------------
# 4. Model Evaluation
# -------------------------------
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)

print("\n--- Model Evaluation ---")
print(f"R² Score: {r2:.2f}")


# -------------------------------
# 5. Predict New House Price
# -------------------------------
print("\n--- Predict House Price ---")

area = float(input("Enter area (sq ft): "))
bedrooms = int(input("Enter number of bedrooms: "))
age = int(input("Enter age of house: "))

new_house = np.array([[area, bedrooms, age]])
predicted_price = model.predict(new_house)

print(f"\nPredicted Price: ₹{predicted_price[0]:,.2f}")


# -------------------------------
# 6. Visualization (Area vs Price)
# -------------------------------
plt.figure()
plt.scatter(df["Area (sq ft)"], y)
plt.plot(df["Area (sq ft)"], model.predict(X), linestyle='dashed')
plt.xlabel("Area (sq ft)")
plt.ylabel("Price")
plt.title("House Price Prediction (Area vs Price)")
plt.show()