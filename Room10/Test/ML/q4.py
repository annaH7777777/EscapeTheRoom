# Q4: What is the output of model.predict(X)?
# Options:
#   - Probabilities
#   - Predicted labels
#   - Accuracy
#   - Coefficients
# Answer: Predicted labels
#
# Explanation:
# In sklearn's API, `.predict(X)` returns the model's final answer for
# each sample in X — for a classifier that means **class labels**, and
# for a regressor that means **numeric predictions**.
# The other quantities come from different methods/attributes:
#   - Probabilities → model.predict_proba(X) (classifiers that support it)
#   - Decision scores → model.decision_function(X)
#   - Accuracy → model.score(X, y) (compares predictions vs true labels)
#   - Coefficients → model.coef_ and model.intercept_ (linear models only)
# So `.predict()` is always the "give me the final answer" call.


import numpy as np
from sklearn.linear_model import LogisticRegression

X = np.array([[1, 1], [2, 1], [6, 7], [7, 7]])
y = np.array([0, 0, 1, 1])

model = LogisticRegression().fit(X, y)

X_new = np.array([[2, 2], [7, 6]])

print(f"predict           : {model.predict(X_new).tolist()}")           # [0, 1] -> labels
print(f"predict_proba     :\n{model.predict_proba(X_new).round(3)}")     # probabilities
print(f"decision_function : {model.decision_function(X_new).round(3)}")  # raw scores
print(f"score(X, y)       : {model.score(X, y):.2f}")                    # accuracy
print(f"coef_             : {model.coef_.round(2)}")                     # learned weights
print(f"intercept_        : {model.intercept_.round(2)}")                # bias term
