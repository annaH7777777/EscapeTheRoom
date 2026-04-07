#Fix the Logistic Regression training mistake.

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression()

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', model)
])

pipe.fit(X_train, y_train)
print("Test accuracy:", pipe.score(X_test, y_test))

