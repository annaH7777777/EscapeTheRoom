#Fix the order of operations and ensure the model is trained using proper data structures before prediction.

from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.array([[0.1, 0.2], [0.3, 0.4]])
y = np.array([0, 1])

model = LogisticRegression()
model.fit(X, y)
predictions = model.predict(X)
print(predictions)
