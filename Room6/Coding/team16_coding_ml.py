#Write a function that splits a dataset and manually balances the training set for equal class representation.

import numpy as np
from sklearn.model_selection import train_test_split


def split_and_balance(X, y, test_size=0.2, random_state=42):
    # Step 1: split into train/test (80/20 by default)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    # Step 2: find all unique classes and how many samples each has
    # e.g. classes=[0,1,2], counts=[120,24,16]
    classes, counts = np.unique(y_train, return_counts=True)
    # Step 3: find the smallest class — we'll downsample all others to this size
    # e.g. min_count=16 (class 2 has fewest)
    min_count = counts.min()
    balanced_indices = []
    rng = np.random.RandomState(random_state)
    # Step 4: for each class, randomly pick min_count samples
    for cls in classes:
        # get positions in y_train where class == cls
        cls_indices = np.where(y_train == cls)[0]
        # randomly sample min_count indices (no duplicates)
        sampled = rng.choice(cls_indices, size=min_count, replace=False)
        balanced_indices.extend(sampled)
    # Step 5: shuffle so classes aren't in order
    rng.shuffle(balanced_indices)
    # Step 6: use the balanced indices to get the final training data
    X_train_balanced = X_train[balanced_indices]
    y_train_balanced = y_train[balanced_indices]
    # test set stays unchanged — we only balance training
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