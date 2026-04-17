# Q4: What is a feature?
# Options:
#   - Output label
#   - Input variable
#   - Column name
#   - Metric
# Answer: Input variable
#
# Explanation:
# A "feature" is an INPUT variable the model uses to make predictions
# — one measurable property of a sample. Together, all features form
# the feature matrix X.
# Contrast:
#   - "Output label" → the target y the model tries to predict.
#   - "Column name"  → just the header/name of a column in a DataFrame
#                      (a feature's name is a column name, but a column
#                      name by itself is not the feature — the VALUES are).
#   - "Metric"       → a measure of model quality (accuracy, RMSE, ...).
# In sklearn's convention:
#   - X → features (rows = samples, columns = features)
#   - y → labels


import numpy as np
from sklearn.linear_model import LogisticRegression

# Each row is a sample; each COLUMN is a feature (an input variable)
# Features here: age, income
feature_names = ["age", "income"]
X = np.array([
    [22, 20_000],
    [25, 25_000],
    [30, 40_000],
    [45, 80_000],
    [50, 90_000],
    [60, 120_000],
])
y = np.array([0, 0, 0, 1, 1, 1])    # the label — NOT a feature

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

print(f"Feature names        : {feature_names}")
print(f"X shape (samples, features): {X.shape}")     # (6, 2) → 2 features
print(f"Label y              : {y}")
print(f"Learned coefficients : {model.coef_[0]}")     # one weight per feature
