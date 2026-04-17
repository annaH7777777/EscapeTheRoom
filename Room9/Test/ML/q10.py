# Q10: What is cross-validation used for?
# Options:
#   - Visualizing errors
#   - Selecting features
#   - Validating model on different splits
#   - Normalizing data
# Answer: Validating model on different splits
#
# Explanation:
# Cross-validation (CV) estimates how well a model generalizes by
# evaluating it on SEVERAL different train/test splits rather than
# a single hold-out set. The most common variant, k-fold CV:
#   1. Divide the data into k equal folds.
#   2. For each fold i: train on the other k-1 folds, evaluate on fold i.
#   3. Average the k scores → a more reliable estimate of model quality.
# Benefits:
#   - Reduces the luck/unluck of a single train/test split.
#   - Uses every sample for both training and validation (but never both
#     in the same fold).
# Not what CV does:
#   - "Visualizing errors"  → plotting / inspection, not CV.
#   - "Selecting features"  → feature selection uses CV internally
#                             sometimes, but CV itself does not pick features.
#   - "Normalizing data"    → preprocessing (StandardScaler etc.).


import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, KFold

rng = np.random.default_rng(0)
X = rng.normal(size=(60, 2))
y = (X[:, 0] + X[:, 1] > 0).astype(int)

model = LogisticRegression()

# 5-fold CV → 5 accuracy scores, one per held-out fold
scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
print(f"Per-fold accuracy : {scores.round(3).tolist()}")
print(f"Mean accuracy     : {scores.mean():.3f}")
print(f"Std across folds  : {scores.std():.3f}")

# Manual loop with KFold to show what cross_val_score does internally
kf = KFold(n_splits=5, shuffle=True, random_state=0)
manual_scores = []
for fold, (train_idx, test_idx) in enumerate(kf.split(X), start=1):
    model.fit(X[train_idx], y[train_idx])
    fold_acc = model.score(X[test_idx], y[test_idx])
    manual_scores.append(fold_acc)
    print(f"fold {fold}: train={len(train_idx)}, test={len(test_idx)}, acc={fold_acc:.3f}")

print(f"Manual mean acc   : {np.mean(manual_scores):.3f}")
