#Fix the model training pipeline to correctly scale data before Logistic Regression.

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

pipe.fit(X_train, y_train)

import numpy as np
scaler = pipe.named_steps["scaler"]
X_scaled = scaler.transform(X_train)
print(f"Before scaling: {X_train[:3]}")
print(f"After scaling:  {np.round(X_scaled[:3], 2)}")

print(f"Accuracy: {pipe.score(X_test, y_test):.2f}")
