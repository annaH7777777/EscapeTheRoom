#How do you check the feature importance in decision trees?
#feature_importances_

from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
model = DecisionTreeClassifier()
model.fit(X, y)

feature_names = load_iris().feature_names
for name, importance in zip(feature_names, model.feature_importances_):
    print(f"{name}: {importance:.4f}")