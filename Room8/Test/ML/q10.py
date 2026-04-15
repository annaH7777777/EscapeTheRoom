# Q10: Which metric is used for classification?
# Options:
#   - MSE
#   - Accuracy
#   - RMSE
#   - MAE
# Answer: Accuracy
#
# Explanation:
# Metrics split by task:
#   CLASSIFICATION (discrete labels):
#       accuracy, precision, recall, F1, ROC-AUC, log loss, confusion matrix
#   REGRESSION (numeric values):
#       MSE  (Mean Squared Error)       - average squared error
#       RMSE (Root Mean Squared Error)  - sqrt(MSE), same units as target
#       MAE  (Mean Absolute Error)      - average absolute error
#       R^2  (coefficient of determination)
#
# MSE/RMSE/MAE measure how close predicted NUMBERS are to true NUMBERS,
# so they don't make sense for class labels. Accuracy is the basic
# classification metric (though F1/AUC are better on imbalanced data).


import numpy as np
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    mean_squared_error, mean_absolute_error, r2_score,
)

# --- Classification metrics ---
y_true_cls = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0])
y_pred_cls = np.array([1, 0, 1, 0, 0, 1, 1, 0, 1, 0])

print("Classification metrics:")
print(f"  accuracy  = {accuracy_score(y_true_cls, y_pred_cls):.2f}")
print(f"  precision = {precision_score(y_true_cls, y_pred_cls):.2f}")
print(f"  recall    = {recall_score(y_true_cls, y_pred_cls):.2f}")
print(f"  f1        = {f1_score(y_true_cls, y_pred_cls):.2f}")

# --- Regression metrics (for contrast) ---
y_true_reg = np.array([3.0, 5.0, 7.0, 9.0, 11.0])
y_pred_reg = np.array([2.8, 5.2, 6.9, 9.1, 10.8])

mse = mean_squared_error(y_true_reg, y_pred_reg)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_true_reg, y_pred_reg)

print("\nRegression metrics:")
print(f"  MSE  = {mse:.4f}")
print(f"  RMSE = {rmse:.4f}")
print(f"  MAE  = {mae:.4f}")
print(f"  R^2  = {r2_score(y_true_reg, y_pred_reg):.4f}")
