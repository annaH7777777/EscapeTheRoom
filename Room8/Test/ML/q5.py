# Q5: What is normalization?
# Options:
#   - Centering data
#   - Scaling values to 0-1
#   - Encoding classes
#   - Removing nulls
# Answer: Scaling values to 0-1
#
# Explanation:
# Normalization rescales numeric features into a fixed range,
# typically [0, 1], using min-max scaling:
#     x_norm = (x - min) / (max - min)
# This is useful when features have very different scales (e.g. age 0-100
# vs. income 0-100_000) — models sensitive to distance/magnitude
# (kNN, neural nets, gradient descent) train better on comparable ranges.
#
# Contrast with the other options:
#   - Centering data (subtract the mean) -> part of STANDARDIZATION (z-score),
#     which uses StandardScaler, not MinMaxScaler.
#   - Encoding classes -> turning categories into numbers (LabelEncoder,
#     OneHotEncoder).
#   - Removing nulls  -> imputation / dropping (SimpleImputer, dropna).


import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Two features on very different scales
X = np.array([
    [  25,  30_000],
    [  40,  60_000],
    [  60, 120_000],
    [  35,  80_000],
])

scaler = MinMaxScaler()           # default range is [0, 1]
X_norm = scaler.fit_transform(X)

print("Original:")
print(X)
print("\nNormalized to [0, 1]:")
print(X_norm)
print(f"\nMin per column (normalized): {X_norm.min(axis=0)}")   # [0. 0.]
print(f"Max per column (normalized): {X_norm.max(axis=0)}")     # [1. 1.]
