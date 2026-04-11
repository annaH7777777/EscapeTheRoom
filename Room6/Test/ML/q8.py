# Q8 (ML): What happens if a model underfits?
# Answer: Poor performance on both train and test

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Non-linear data: y = x^2 + noise
np.random.seed(42)
X_train = np.sort(np.random.uniform(0, 10, 50)).reshape(-1, 1)
y_train = X_train.ravel() ** 2 + np.random.normal(0, 5, 50)
X_test = np.sort(np.random.uniform(0, 10, 20)).reshape(-1, 1)
y_test = X_test.ravel() ** 2 + np.random.normal(0, 5, 20)

# === Underfit: linear model on non-linear data (too simple) ===
underfit = LinearRegression().fit(X_train, y_train)
print("=== UNDERFIT (Linear Regression on quadratic data) ===")
print(f"  Train MSE: {mean_squared_error(y_train, underfit.predict(X_train)):.2f}")
print(f"  Test MSE:  {mean_squared_error(y_test, underfit.predict(X_test)):.2f}")
print(f"  -> Both are BAD (high error)")

# === Good fit: decision tree with reasonable depth ===
good = DecisionTreeRegressor(max_depth=4).fit(X_train, y_train)
print("\n=== GOOD FIT (DecisionTree max_depth=4) ===")
print(f"  Train MSE: {mean_squared_error(y_train, good.predict(X_train)):.2f}")
print(f"  Test MSE:  {mean_squared_error(y_test, good.predict(X_test)):.2f}")
print(f"  -> Both are GOOD (low error)")

# === Overfit: unlimited depth tree (memorizes training data) ===
overfit = DecisionTreeRegressor(max_depth=None).fit(X_train, y_train)
print("\n=== OVERFIT (DecisionTree unlimited depth) ===")
print(f"  Train MSE: {mean_squared_error(y_train, overfit.predict(X_train)):.2f}")
print(f"  Test MSE:  {mean_squared_error(y_test, overfit.predict(X_test)):.2f}")
print(f"  -> Train is PERFECT, test is WORSE")

# === Summary ===
print("\n=== Summary ===")
print("  Underfit: train BAD,  test BAD   (model too simple)")
print("  Good fit: train GOOD, test GOOD  (model just right)")
print("  Overfit:  train GREAT, test BAD  (model memorized noise)")