import pandas as pd

df = pd.read_csv("D:\Suprmentr Assignments\Assignment 07\job_salary_prediction_dataset.csv")

# ---- 1. Display top rows ----
print("Top 5 rows of the dataset:")
print(df.head())


# ---- 2. Find column with highest value ----
# (Considering only numeric columns)
numeric_cols = df.select_dtypes(include=['number'])

max_values = numeric_cols.max()
highest_column = max_values.idxmax()
highest_value = max_values.max()

print("\nColumn with highest value:")
print("Column:", highest_column)
print("Highest Value:", highest_value)


# ---- 3. Count missing values ----
print("\nMissing values in each column:")
print(df.isnull().sum())


# ---- 4. Basic info (optional but useful) ----
print("\nDataset Info:")
print(df.info())