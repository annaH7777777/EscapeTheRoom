# Q7 (ML): What type of model is KNeighborsClassifier?
# Answer: Non-linear

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

# "Moons" data: non-linear decision boundary (two interleaving half-circles)
X, y = make_moons(n_samples=300, noise=0.2, random_state=42)

knn_score = cross_val_score(KNeighborsClassifier(), X, y, cv=5).mean()
linear_score = cross_val_score(LogisticRegression(), X, y, cv=5).mean()

print(f"KNN (non-linear):           {knn_score:.3f}  <- handles curved boundaries")
print(f"Logistic Regression (linear): {linear_score:.3f}  <- limited by straight line")
print(f"\n-> KNN wins on non-linear data because it has no linear constraint")
