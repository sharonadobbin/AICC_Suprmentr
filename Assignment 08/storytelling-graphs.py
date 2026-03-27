import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Load Dataset
# -------------------------------
# You can replace this with your own dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")

print("First 5 rows of dataset:")
print(df.head())


# -------------------------------
# Data Preprocessing
# -------------------------------
# Drop missing values for simplicity
df = df.dropna()

# -------------------------------
# 1. BAR CHART
# Count of passengers by class
# -------------------------------
class_counts = df['class'].value_counts()

plt.figure()
class_counts.plot(kind='bar')
plt.title("Passenger Count by Class")
plt.xlabel("Class")
plt.ylabel("Number of Passengers")
plt.xticks(rotation=0)
plt.show()


# -------------------------------
# 2. PIE CHART
# Survival distribution
# -------------------------------
survival_counts = df['survived'].value_counts()

plt.figure()
plt.pie(
    survival_counts,
    labels=["Did Not Survive", "Survived"],
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Survival Distribution")
plt.show()


# -------------------------------
# 3. HISTOGRAM
# Age distribution
# -------------------------------
plt.figure()
plt.hist(df['age'], bins=20)
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


# -------------------------------
# Data Story (Printed Output)
# -------------------------------
print("\n--- DATA STORY ---\n")

# Key values for storytelling
most_common_class = class_counts.idxmax()
survival_rate = (survival_counts[1] / survival_counts.sum()) * 100
average_age = df['age'].mean()

print(f"Most passengers were in {most_common_class} class.")
print(f"Overall survival rate was approximately {survival_rate:.2f}%.")
print(f"The average age of passengers was around {average_age:.1f} years.")

print("\nInsights:")
print("1. Lower-class passengers were more in number, indicating economic diversity.")
print("2. Survival rate was less than 50%, showing the severity of the disaster.")
print("3. Most passengers were adults, with fewer children and elderly individuals.")
print("4. Class may have influenced survival chances (higher class likely safer).")
print("5. The dataset shows clear social and survival disparities among passengers.")