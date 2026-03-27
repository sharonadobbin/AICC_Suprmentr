import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# -------------------------------
# 1. Dataset (Mall Customers)
# -------------------------------
data = {
    "Income": [15, 16, 17, 18, 40, 42, 43, 45, 70, 72, 73, 75],
    "Spending": [39, 81, 6, 77, 40, 42, 50, 60, 20, 25, 30, 35]
}

df = pd.DataFrame(data)

# -------------------------------
# 2. Apply K-Means
# -------------------------------
kmeans = KMeans(n_clusters=3, random_state=0)
df["Cluster"] = kmeans.fit_predict(df)

# -------------------------------
# 3. Visualization
# -------------------------------
plt.figure()

for i in range(3):
    cluster = df[df["Cluster"] == i]
    plt.scatter(cluster["Income"], cluster["Spending"], label=f"Cluster {i}")

plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    marker='X',
    s=200,
    label='Centroids'
)

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.legend()
plt.show()

# -------------------------------
# 4. Describe Groups
# -------------------------------
print("\nCustomer Groups:\n")

for i in range(3):
    group = df[df["Cluster"] == i]
    avg_income = group["Income"].mean()
    avg_spending = group["Spending"].mean()

    print(f"Cluster {i}:")
    print(f" Avg Income: {avg_income:.1f}")
    print(f" Avg Spending: {avg_spending:.1f}")

    if avg_income < 30:
        print(" Type: Low income group")
    elif avg_income > 60:
        print(" Type: High income group")
    else:
        print(" Type: Medium income group")

    print()