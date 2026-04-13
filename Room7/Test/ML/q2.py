# Q2 (ML): Which metric is best for skewed class distribution?
# Answer: ROC AUC

import numpy as np
from sklearn.metrics import accuracy_score, roc_auc_score

# Skewed: 95% class 0, 5% class 1
y_true = np.array([0]*95 + [1]*5)

# Lazy model: always predicts majority class
y_pred_lazy = np.array([0]*100)
y_proba_lazy = np.array([0.1]*100)  # same probability for all

print("=== Lazy model (always predicts 0) ===")
print(f"  Accuracy: {accuracy_score(y_true, y_pred_lazy):.2f}  <- misleading! (high)")
print(f"  ROC AUC:  {roc_auc_score(y_true, y_proba_lazy):.2f}  <- correctly shows useless (0.5 = random)")

# Decent model: gives higher probability to real positives
y_proba_decent = np.concatenate([np.random.uniform(0, 0.4, 95), np.random.uniform(0.6, 1.0, 5)])
print("\n=== Decent model ===")
print(f"  ROC AUC:  {roc_auc_score(y_true, y_proba_decent):.2f}  <- 1.0 is perfect, 0.5 is random")
