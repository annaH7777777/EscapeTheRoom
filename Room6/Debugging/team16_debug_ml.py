#Fix the code to correctly create a Pipeline by importing the Pipeline module from sklearn.

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

X, y = load_iris(return_X_y=True)
pipe.fit(X, y)
print(f"Pipeline fitted successfully!")
print(f"Score: {pipe.score(X, y):.4f}")