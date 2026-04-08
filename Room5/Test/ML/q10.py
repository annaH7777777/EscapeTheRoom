#What does PCA aim to do?
#Reduce dimensionality while retaining variance

from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
print(f"Original shape: {X.shape}")  # → (150, 4)

pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)
print(f"Reduced shape: {X_reduced.shape}")  # → (150, 2)
print(f"Variance retained: {sum(pca.explained_variance_ratio_):.2%}")