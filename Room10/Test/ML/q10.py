# Q10: What is a common issue if "ValueError: Expected 2D array, got 1D array instead" occurs?
# Options:
#   - Input shape is incorrect
#   - Missing labels
#   - Data type mismatch
#   - Data not scaled
# Answer: Input shape is incorrect
#
# Explanation:
# Most sklearn estimators expect the feature matrix X to be **2-dimensional**:
# shape (n_samples, n_features). If you pass a 1-D array like [1, 2, 3] or
# a single sample like [2, 5], sklearn can't tell whether it's one row with
# 3 features or 3 rows with 1 feature — so it raises
#     ValueError: Expected 2D array, got 1D array instead.
# Fixes (pick whichever matches your intent):
#   - For a single sample (one row):     X.reshape(1, -1)
#   - For a single feature (one column): X.reshape(-1, 1)
#   - Pass a list of lists / 2-D numpy array directly: [[1, 2, 3]]
# The other options describe different failures:
#   - Missing labels      → raises on .fit(X, y) — different message.
#   - Data type mismatch  → e.g. strings where floats are expected.
#   - Data not scaled     → causes bad accuracy, not a shape error.


import numpy as np
from sklearn.linear_model import LogisticRegression

X = np.array([[1, 1], [2, 1], [1, 2], [6, 7], [7, 7], [8, 6]])
y = np.array([0, 0, 0, 1, 1, 1])
model = LogisticRegression().fit(X, y)

# --- Wrong: 1-D input ---
try:
    bad = np.array([2, 2])                 # shape (2,) — 1-D
    model.predict(bad)
except ValueError as e:
    print(f"ERROR caught:\n  {e}\n")

# --- Fix 1: reshape(1, -1) — one sample with several features ---
good_one_sample = np.array([2, 2]).reshape(1, -1)   # shape (1, 2)
print(f"one sample (1,-1) -> shape {good_one_sample.shape}, pred {model.predict(good_one_sample).tolist()}")

# --- Fix 2: wrap in another list — same effect ---
good_list = [[2, 2], [7, 6]]                        # shape (2, 2)
print(f"list of lists     -> pred {model.predict(good_list).tolist()}")

# --- When to use reshape(-1, 1): a single feature for several samples ---
single_feature = np.array([1, 2, 3, 4, 5])          # 1-D
as_column = single_feature.reshape(-1, 1)           # shape (5, 1)
print(f"\nsingle feature reshaped to column: {as_column.shape}")
