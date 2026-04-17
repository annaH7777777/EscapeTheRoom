# Q7: What does .predict() return?
# Options:
#   - True labels
#   - Predictions
#   - Probabilities
#   - Features
# Answer: Predictions
#
# Explanation:
# .predict(X) asks a trained model to make PREDICTIONS for new inputs:
#   - For a classifier → returns the predicted CLASS LABELS
#     (one label per row of X).
#   - For a regressor  → returns the predicted NUMERIC VALUES.
# Not to be confused with:
#   - "True labels" → the ground truth y, which you provide (never returned
#                     by a model).
#   - "Probabilities" → returned by .predict_proba(X) for classifiers that
#                       support it (e.g. LogisticRegression).
#   - "Features"     → the inputs X; the model CONSUMES them, never returns them.


import numpy as np
from sklearn.linear_model import LogisticRegression

X = np.array([
    [1, 1], [2, 1], [1, 2],
    [6, 7], [7, 7], [8, 6],
])
y = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

X_new = np.array([[2, 2], [7, 6]])

preds  = model.predict(X_new)           # predicted class LABELS
probs  = model.predict_proba(X_new)     # predicted PROBABILITIES per class

print(f"predict(X_new)       -> {preds.tolist()}")   # e.g. [0, 1]
print(f"predict_proba(X_new) ->\n{probs.round(3)}")
print(f"classes_             -> {model.classes_.tolist()}")
# Each row of probs sums to 1 across the classes
print(f"row sums             -> {probs.sum(axis=1).tolist()}")
