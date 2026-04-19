# Q7: Which evaluation metric is most common for classification?
# Options:
#   - MAE
#   - RMSE
#   - Accuracy
#   - Loss
# Answer: Accuracy
#
# Explanation:
# Accuracy = (correct predictions) / (total predictions). It's the default,
# most intuitive metric for classification and what sklearn's `.score()`
# returns for classifiers.
# Why the others don't fit:
#   - MAE (Mean Absolute Error) and RMSE (Root Mean Squared Error) are
#     REGRESSION metrics — they measure how far numeric predictions are
#     from numeric targets, which doesn't apply to discrete class labels.
#   - "Loss" (e.g. cross-entropy, hinge loss) is what the model minimizes
#     DURING training. It's not a standard reporting metric for "how good
#     is my classifier?"
# Caveat: for imbalanced datasets (say 99% class 0, 1% class 1), accuracy
# is misleading — a dumb "always predict 0" model scores 99%. Prefer
# precision, recall, F1, or ROC-AUC in those cases.


import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

X = np.array([[1, 1], [2, 1], [1, 2], [6, 7], [7, 7], [8, 6]])
y = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression().fit(X, y)
y_pred = model.predict(X)

print(f"accuracy  : {accuracy_score(y, y_pred):.2f}")
print(f".score()  : {model.score(X, y):.2f}")         # same as accuracy for classifiers
print(f"precision : {precision_score(y, y_pred):.2f}")
print(f"recall    : {recall_score(y, y_pred):.2f}")
print(f"f1        : {f1_score(y, y_pred):.2f}")

# Imbalance warning demo
y_true = np.array([0] * 99 + [1])
y_dumb = np.zeros(100, dtype=int)        # always predicts class 0
print(f"\nimbalanced accuracy : {accuracy_score(y_true, y_dumb):.2f}")  # 0.99 — misleading!
print(f"imbalanced recall   : {recall_score(y_true, y_dumb):.2f}")     # 0.00 — reveals it
