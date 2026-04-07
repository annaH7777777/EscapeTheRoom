#What does overfitting indicate?
#Good training score, bad test score

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Overfit: no depth limit, tree memorizes training data
model = DecisionTreeClassifier(max_depth=None, random_state=42)
model.fit(X_train, y_train)

print("Train score:", model.score(X_train, y_train))  # ~1.0 (perfect)
print("Test score:", model.score(X_test, y_test))      # lower — overfitting gap