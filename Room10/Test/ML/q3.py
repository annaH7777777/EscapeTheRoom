# Q3: Which class is used for logistic regression?
# Options:
#   - LogisticRegressor
#   - LogisticRegression
#   - LinearRegression
#   - ClassifyLogit
# Answer: LogisticRegression
#
# Explanation:
# sklearn.linear_model.LogisticRegression is a *classification* model,
# despite the word "regression" in its name. It estimates the probability
# that an input belongs to each class using the sigmoid/softmax function
# and returns a class label via .predict() (and probabilities via
# .predict_proba()).
# Watch out for the common traps:
#   - "LogisticRegressor"  — does not exist in sklearn.
#   - "LinearRegression"   — predicts continuous numbers (regression),
#                            not class labels. Wrong tool for classification.
#   - "ClassifyLogit"      — made-up name, not an sklearn class.


import numpy as np
from sklearn.linear_model import LogisticRegression

X = np.array([
    [1, 1], [2, 1], [1, 2],
    [6, 7], [7, 7], [8, 6],
])
y = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

# .predict() returns class labels
print(f"predictions     : {model.predict([[2, 2], [7, 6]]).tolist()}")   # [0, 1]

# .predict_proba() returns class probabilities (columns = classes)
probs = model.predict_proba([[2, 2], [7, 6]])
print(f"probabilities   :\n{probs.round(3)}")

print(f"coefficients    : {model.coef_.round(2)}")
print(f"accuracy (train): {model.score(X, y):.2f}")
