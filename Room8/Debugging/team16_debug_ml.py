#Fix the code so the model is fitted.

from sklearn.linear_model import LogisticRegression
import numpy as np

# Example data (2 samples, 2 features)
X = np.array([[0, 1], [1, 1]])
y = np.array([0, 1])

model = LogisticRegression()
model.fit(X, y)
probs = model.predict_proba(X)
print(probs)
