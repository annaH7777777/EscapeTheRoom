#Fix the training step so the model is trained on the correct training data.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

print(f"Train score: {model.score(X_train, y_train):.3f}")
print(f"Test score:  {model.score(X_test, y_test):.3f}")