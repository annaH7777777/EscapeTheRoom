# Q8: What does .score() typically return for classifiers?
# Options:
#   - Loss
#   - Accuracy
#   - RMSE
#   - AUC
# Answer: Accuracy
#
# Explanation:
# For sklearn CLASSIFIERS, .score(X, y) returns ACCURACY by default —
# the fraction of samples whose predicted label matches the true label:
#     accuracy = correct / total       (range 0.0 – 1.0)
# For REGRESSORS, .score(X, y) returns the R² (coefficient of
# determination), not RMSE.
# Other metrics need explicit computation:
#   - Loss → from a loss function (log_loss, hinge, ...)
#   - RMSE → for regression (sqrt of mean squared error)
#   - AUC  → roc_auc_score, needs probability/score output


import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X = np.array([
    [1, 1], [2, 1], [1, 2],
    [6, 7], [7, 7], [8, 6],
])
y = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

# .score() for a classifier == accuracy
score = model.score(X, y)
preds = model.predict(X)
acc   = accuracy_score(y, preds)

print(f"model.score(X, y)     -> {score:.4f}")   # same number …
print(f"accuracy_score(y, ^)  -> {acc:.4f}")     # … as this one
print(f"Predictions           -> {preds.tolist()}")
print(f"True labels           -> {y.tolist()}")
print(f"Correct / total       -> {(preds == y).sum()} / {len(y)}")
