#What does cross-validation help with?
#Overfitting

from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
model = DecisionTreeClassifier()

scores = cross_val_score(model, X, y, cv=5)
print(f"Scores: {scores}")
print(f"Mean: {scores.mean():.2f}")