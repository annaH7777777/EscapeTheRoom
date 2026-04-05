#Which is a type of dimensionality reduction?
#PCA

from sklearn.decomposition import PCA
import numpy as np

# Create some fake data: 10 samples, 5 features
X = np.array([
    [2.5, 2.4, 1.2, 3.1, 0.5],
    [0.5, 0.7, 0.3, 1.2, 0.1],
    [2.2, 2.9, 1.8, 2.8, 0.4],
    [1.9, 2.2, 1.5, 2.5, 0.3],
    [3.1, 3.0, 2.1, 3.5, 0.6],
    [2.3, 2.7, 1.7, 2.9, 0.5],
    [2.0, 1.6, 1.1, 2.2, 0.2],
    [1.0, 1.1, 0.8, 1.5, 0.1],
    [1.5, 1.6, 1.0, 1.8, 0.2],
    [1.1, 0.9, 0.6, 1.3, 0.1],
])

print("Original shape:", X.shape)   # → (10, 5) — 5 features

# Reduce to 2 dimensions
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print("Reduced shape:", X_reduced.shape)  # → (10, 2) — 2 features!
print("Variance kept:", pca.explained_variance_ratio_.sum())  # → ~0.99
print(X_reduced)