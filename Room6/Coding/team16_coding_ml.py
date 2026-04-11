#Write a function that splits a dataset and manually balances the training set for equal class representation.

import numpy as np
from sklearn.model_selection import train_test_split


def split_and_balance(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    classes, counts = np.unique(y_train, return_counts=True)
    min_count = counts.min()
    balanced_indices = []
    rng = np.random.RandomState(random_state)
    for cls in classes:
        cls_indices = np.where(y_train == cls)[0]
        sampled = rng.choice(cls_indices, size=min_count, replace=False)
        balanced_indices.extend(sampled)
    rng.shuffle(balanced_indices)
    X_train_balanced = X_train[balanced_indices]
    y_train_balanced = y_train[balanced_indices]
    return X_train_balanced, X_test, y_train_balanced, y_test


# === Test with imbalanced data ===
np.random.seed(42)
X = np.random.randn(200, 3)
y = np.array([0]*150 + [1]*30 + [2]*20)  # imbalanced: 150, 30, 20

print("=== Original dataset ===")
classes, counts = np.unique(y, return_counts=True)
for cls, cnt in zip(classes, counts):
    print(f"  Class {cls}: {cnt} samples")

X_train_bal, X_test, y_train_bal, y_test = split_and_balance(X, y)

print("\n=== Balanced training set ===")
classes, counts = np.unique(y_train_bal, return_counts=True)
for cls, cnt in zip(classes, counts):
    print(f"  Class {cls}: {cnt} samples")
print(f"  Total: {len(y_train_bal)} samples (equal per class)")

print("\n=== Test set (unchanged) ===")
classes, counts = np.unique(y_test, return_counts=True)
for cls, cnt in zip(classes, counts):
    print(f"  Class {cls}: {cnt} samples")
print(f"  Total: {len(y_test)} samples")