import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# -------------------------------
# 1. Create Dataset (Sample Mall Data)
# -------------------------------
data = {
    "Annual Income (k$)": [15, 16, 17, 18, 40, 42, 43, 45, 70, 72, 73, 75],
    "Spending Score": [39, 81, 6, 77, 40, 42, 50, 60, 20, 25, 30, 35]
}

df = pd.DataFrame(data)

print("\n--- Dataset ---")
print(df)


# -------------------------------
# 2. Apply K-Means Clustering
# -------------------------------
kmeans = KMeans(n_clusters=3, random_state=0)
df["Cluster"] = kmeans.fit_predict(df)

print("\n--- Clustered Data ---")
print(df)


# -------------------------------
# 3. Visualization
# -------------------------------
plt.figure()

for i in range(3):
    cluster = df[df["Cluster"] == i]
    plt.scatter(cluster["Annual Income (k$)"], cluster["Spending Score"], label=f"Cluster {i}")

# Plot centroids
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, label='Centroids')

plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.legend()
plt.show()


# -------------------------------
# 4. Description of Clusters
# -------------------------------
print("\n--- Customer Groups ---")

for i in range(3):
    group = df[df["Cluster"] == i]
    avg_income = group["Annual Income (k$)"].mean()
    avg_spending = group["Spending Score"].mean()

    print(f"\nCluster {i}:")
    print(f"Average Income: {avg_income:.2f}")
    print(f"Average Spending Score: {avg_spending:.2f}")

    if avg_income < 30:
        print("Type: Low Income Customers")
    elif avg_income > 60:
        print("Type: High Income Customers")
    else:
        print("Type: Medium Income Customers")