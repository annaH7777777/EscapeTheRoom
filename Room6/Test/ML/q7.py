# Q7 (ML): Which technique reduces dimensionality?
# Answer: Principal component analysis (PCA)

import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# Load Iris: 4 features
X, y = load_iris(return_X_y=True)
print(f"=== Original data ===")
print(f"  Shape: {X.shape}  (150 samples, 4 features)")
print(f"  Features: sepal_length, sepal_width, petal_length, petal_width")

# === PCA: reduce 4 features -> 2 components ===
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)
print(f"\n=== After PCA (4 -> 2) ===")
print(f"  Shape: {X_reduced.shape}  (150 samples, 2 components)")

# How much information is preserved?
print(f"\n=== Explained variance ===")
print(f"  Component 1: {pca.explained_variance_ratio_[0]:.2%}")
print(f"  Component 2: {pca.explained_variance_ratio_[1]:.2%}")
print(f"  Total:       {sum(pca.explained_variance_ratio_):.2%} of variance kept")
print(f"  Lost only {1 - sum(pca.explained_variance_ratio_):.2%} by dropping 2 features!")

# === How many components to keep? ===
print(f"\n=== All components' variance ===")
pca_full = PCA().fit(X)
cumulative = np.cumsum(pca_full.explained_variance_ratio_)
for i, (var, cum) in enumerate(zip(pca_full.explained_variance_ratio_, cumulative)):
    print(f"  Component {i+1}: {var:.2%}  (cumulative: {cum:.2%})")