#What does PCA mainly do?
#Dimensionality reduction

from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
print("Original shape:", X.shape)  # (150, 4) — 4 features

pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)
print("Reduced shape:", X_reduced.shape)  # (150, 2) — 2 features

print("Explained variance ratio:", pca.explained_variance_ratio_)