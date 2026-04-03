#Fix the sklearn pipeline code so it runs without error and fits the model properly.

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import numpy as np

# Minimal synthetic dataset
X = np.array([[0.1, 1.2], [1.1, 0.9], [0.3, 1.0], [1.2, 0.8]])
y = np.array([0, 1, 0, 1])

# Correctly named pipeline steps
pipe = Pipeline([
	('scaler', StandardScaler()),
	('clf', LogisticRegression())
])
pipe.fit(X, y)
print("Pipeline trained successfully.")
# Predict for a new, unseen data sample
new_sample = np.array([[12.0, 14.1]])
print("Prediction for new sample:", pipe.predict(new_sample))
#You can use this one to check print(pipe.predict([X[0]])). It will output a predicted class label like [0], [1], etc.