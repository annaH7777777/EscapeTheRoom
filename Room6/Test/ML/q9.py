# Q9 (ML): What metric is best for highly imbalanced binary classification?
# Answer: F1 Score

import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# Imbalanced dataset: 95% class 0, 5% class 1
np.random.seed(42)
y_true = np.array([0]*95 + [1]*5)

# === Lazy model: always predicts majority class (0) ===
y_pred_lazy = np.array([0]*100)

print("=== Lazy model (always predicts 0) ===")
print(f"  Accuracy:  {accuracy_score(y_true, y_pred_lazy):.2f}  <- looks great! (but useless)")
print(f"  Precision: {precision_score(y_true, y_pred_lazy, zero_division=0):.2f}  <- no positive predictions")
print(f"  Recall:    {recall_score(y_true, y_pred_lazy):.2f}  <- missed ALL positives")
print(f"  F1 Score:  {f1_score(y_true, y_pred_lazy):.2f}  <- correctly shows model is BAD")

# === Decent model: finds some positives ===
y_pred_decent = np.array([0]*92 + [1]*3 + [0]*2 + [1]*3)

print("\n=== Decent model ===")
print(f"  Accuracy:  {accuracy_score(y_true, y_pred_decent):.2f}")
print(f"  Precision: {precision_score(y_true, y_pred_decent):.2f}")
print(f"  Recall:    {recall_score(y_true, y_pred_decent):.2f}")
print(f"  F1 Score:  {f1_score(y_true, y_pred_decent):.2f}  <- balanced view")

# === F1 formula ===
p = precision_score(y_true, y_pred_decent)
r = recall_score(y_true, y_pred_decent)
f1_manual = 2 * (p * r) / (p + r)
print(f"\n=== F1 Formula ===")
print(f"  F1 = 2 * (precision * recall) / (precision + recall)")
print(f"  F1 = 2 * ({p:.2f} * {r:.2f}) / ({p:.2f} + {r:.2f}) = {f1_manual:.2f}")

# === Why accuracy fails ===
print("\n=== Why accuracy is misleading ===")
print(f"  95% accuracy by predicting ALL zeros — learned nothing!")
print(f"  F1=0.00 correctly exposes this as a useless model")
