# Q1 (ML): What does StratifiedKFold ensure?
# Answer: Equal class distribution across folds

import numpy as np
from sklearn.model_selection import KFold, StratifiedKFold

# Imbalanced dataset: 90% class 0, 10% class 1
X = np.arange(20).reshape(-1, 1)
y = np.array([0]*18 + [1]*2)  # 18 zeros, 2 ones
print(f"Full dataset class distribution: 0={sum(y==0)}, 1={sum(y==1)}")
print(f"Class 1 ratio: {sum(y==1)/len(y):.0%}")

# === Regular KFold — no class balance guarantee ===
print("\n=== Regular KFold (no stratification) ===")
kf = KFold(n_splits=5, shuffle=False)
for i, (train_idx, test_idx) in enumerate(kf.split(X)):
    y_test = y[test_idx]
    print(f"  Fold {i+1}: test class 0={sum(y_test==0)}, class 1={sum(y_test==1)}"
          f"  (class 1 ratio: {sum(y_test==1)/len(y_test):.0%})")

# === StratifiedKFold — preserves class ratio in each fold ===
print("\n=== StratifiedKFold (equal class distribution) ===")
skf = StratifiedKFold(n_splits=5, shuffle=False)
for i, (train_idx, test_idx) in enumerate(skf.split(X, y)):
    y_test = y[test_idx]
    print(f"  Fold {i+1}: test class 0={sum(y_test==0)}, class 1={sum(y_test==1)}"
          f"  (class 1 ratio: {sum(y_test==1)/len(y_test):.0%})")

print("\n=== Conclusion ===")
print("StratifiedKFold keeps ~10% class 1 in EVERY fold,")
print("while regular KFold may put all class 1 samples in one fold.")