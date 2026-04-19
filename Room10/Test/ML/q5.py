# Q5: What does StandardScaler() do?
# Options:
#   - Removes rows
#   - Standardizes feature scale
#   - Creates dummy variables
#   - Normalizes labels
# Answer: Standardizes feature scale
#
# Explanation:
# StandardScaler transforms each feature so it has mean = 0 and standard
# deviation = 1 (aka "z-score standardization"):
#     z = (x - mean) / std
# Why scale at all? Models that rely on distances or on the magnitude of
# coefficients (kNN, SVM with RBF kernel, logistic regression, linear
# regression with regularization, PCA, neural networks) get biased when
# one feature's range dwarfs another (e.g. salary in 10000s vs age in 10s).
# Important:
#   - Fit the scaler on the TRAIN set only, then .transform() both train
#     and test — otherwise test statistics leak into training.
#   - StandardScaler operates on **features (X)**, not on labels (y).
#   - Tree-based models (RandomForest, XGBoost) don't need scaling.
# The other options are wrong:
#   - "Removes rows"           — dropping rows is .dropna(), not scaling.
#   - "Creates dummy variables"— that's OneHotEncoder / pd.get_dummies.
#   - "Normalizes labels"      — scalers apply to X, not y.


import numpy as np
from sklearn.preprocessing import StandardScaler

# Two features on VERY different scales: age (10s) vs salary (10000s)
X = np.array([
    [25,  50000],
    [32,  60000],
    [47, 120000],
    [51, 150000],
    [23,  40000],
], dtype=float)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(f"mean before : {X.mean(axis=0)}")              # far from 0
print(f"std  before : {X.std(axis=0)}")               # very different per column

print(f"mean after  : {X_scaled.mean(axis=0).round(3)}")   # ~0
print(f"std  after  : {X_scaled.std(axis=0).round(3)}")    # ~1

print(f"\nscaled:\n{X_scaled.round(3)}")
