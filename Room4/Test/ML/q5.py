#Which algorithm is unsupervised?
#KMeans

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate sample data with 3 natural clusters
X, _ = make_blobs(n_samples=150, centers=3, random_state=42)

# KMeans finds clusters without knowing the labels
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

print("Cluster labels:", kmeans.labels_)
print("Cluster centers:\n", kmeans.cluster_centers_)