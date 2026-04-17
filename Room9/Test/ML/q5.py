# Q5: What does StandardScaler().fit_transform(X) do?
# Options:
#   - Splits X
#   - Converts to integer
#   - Standardizes data
#   - Summarizes features
# Answer: Standardizes data
#
# Explanation:
# StandardScaler transforms each feature to have mean = 0 and std = 1:
#     x' = (x - mean) / std
# fit_transform does both steps in one call:
#   - fit()      → computes the mean and std of each column from X
#   - transform()→ applies (x - mean) / std using those stored stats
# Why it matters:
#   - Distance-based models (kNN, SVM with RBF, k-means) and gradient-based
#     optimizers (logistic/linear regression, neural nets) work much better
#     when features share a similar scale.
# IMPORTANT leakage rule:
#   - fit ONLY on training data; then transform() (NOT fit_transform) on
#     the test data — otherwise test statistics leak into training.


import numpy as np
from sklearn.preprocessing import StandardScaler

# Two features with very different scales: age (~20–60) and income (~20k–120k)
X = np.array([
    [22, 20_000],
    [25, 25_000],
    [30, 40_000],
    [45, 80_000],
    [50, 90_000],
    [60, 120_000],
], dtype=float)

scaler = StandardScaler()
X_std = scaler.fit_transform(X)

print(f"Original means : {X.mean(axis=0)}")
print(f"Original stds  : {X.std(axis=0)}")
print(f"Scaled values:\n{X_std.round(3)}")
print(f"Scaled means   : {X_std.mean(axis=0).round(10)}")   # ≈ [0, 0]
print(f"Scaled stds    : {X_std.std(axis=0).round(10)}")    # ≈ [1, 1]

# Correct workflow — fit on train, only transform on test:
X_train, X_test = X[:4], X[4:]
scaler2 = StandardScaler().fit(X_train)
X_train_s = scaler2.transform(X_train)
X_test_s  = scaler2.transform(X_test)          # reuse train stats — no leakage
print(f"X_test scaled  :\n{X_test_s.round(3)}")
