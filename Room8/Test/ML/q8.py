# Q8: What shape is expected for input X in sklearn?
# Options:
#   - 1D list
#   - 2D array or DataFrame
#   - String
#   - Tuple
# Answer: 2D array or DataFrame
#
# Explanation:
# Sklearn always expects X to be 2D with shape (n_samples, n_features):
#   - rows    = samples
#   - columns = features
# Acceptable: numpy 2D array, pandas DataFrame, scipy sparse matrix, list of lists.
# y, the target, is usually 1D: shape (n_samples,).
# Passing a 1D X raises a ValueError asking you to reshape with .reshape(-1, 1).


import numpy as np
from sklearn.linear_model import LinearRegression

# Correct: X is 2D (5 samples, 1 feature)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

print(f"X shape: {X.shape}  (samples, features)")   # (5, 1)
print(f"y shape: {y.shape}")                        # (5,)

model = LinearRegression().fit(X, y)
print(f"predict([[6]]) = {model.predict([[6]])}")

# Wrong: 1D X raises an error
X_wrong = np.array([1, 2, 3, 4, 5])
print(f"\nX_wrong shape: {X_wrong.shape}  <- 1D, sklearn will reject it")
try:
    LinearRegression().fit(X_wrong, y)
except ValueError as e:
    print(f"ValueError: {str(e).splitlines()[0]}")

# Fix: reshape to 2D
X_fixed = X_wrong.reshape(-1, 1)        # -1 = "figure it out", 1 feature column
print(f"After reshape(-1, 1): {X_fixed.shape}")
LinearRegression().fit(X_fixed, y)       # works now
