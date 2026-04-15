# Q9: Which function evaluates model performance?
# Options:
#   - model.score()
#   - model.split()
#   - model.fit()
#   - model.describe()
# Answer: model.score()
#
# Explanation:
# Every sklearn estimator provides .score(X, y) to evaluate how well
# the trained model does on labeled data. It returns a single number:
#   - Classifiers: accuracy
#   - Regressors:  R^2 (coefficient of determination)
# The other options:
#   - model.split()    -> not a method; splitting is train_test_split()
#   - model.fit()      -> trains the model (doesn't evaluate)
#   - model.describe() -> not a sklearn method (that's pandas)
#
# For more detailed evaluation, use sklearn.metrics (accuracy_score,
# precision_score, recall_score, f1_score, mean_squared_error, r2_score, ...).


import numpy as np
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import train_test_split

# --- Classifier: .score() returns ACCURACY ---
X_cls = np.array([[i, i + 1] for i in range(20)])
y_cls = np.array([0] * 10 + [1] * 10)
Xc_tr, Xc_te, yc_tr, yc_te = train_test_split(X_cls, y_cls, test_size=0.3, random_state=0)

clf = LogisticRegression().fit(Xc_tr, yc_tr)
print(f"Classifier .score() (accuracy): {clf.score(Xc_te, yc_te):.3f}")

# --- Regressor: .score() returns R^2 ---
X_reg = np.arange(20).reshape(-1, 1)
y_reg = 3 * X_reg.ravel() + 7 + np.random.default_rng(0).normal(0, 1, 20)
Xr_tr, Xr_te, yr_tr, yr_te = train_test_split(X_reg, y_reg, test_size=0.3, random_state=0)

reg = LinearRegression().fit(Xr_tr, yr_tr)
print(f"Regressor  .score() (R^2):      {reg.score(Xr_te, yr_te):.3f}")
