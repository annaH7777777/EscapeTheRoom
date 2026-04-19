# Q2: Which sklearn function splits data into train/test sets?
# Options:
#   - split_data()
#   - train_test_split()
#   - train()
#   - partition()
# Answer: train_test_split()
#
# Explanation:
# `sklearn.model_selection.train_test_split` is the canonical way to split
# a dataset into a training set (used to fit the model) and a test set
# (used to evaluate how it generalizes to unseen data).
# Key arguments:
#   - test_size: fraction (e.g. 0.2 = 20% test) or absolute count.
#   - random_state: integer seed for reproducible splits.
#   - stratify=y: keep the class proportions in train and test equal —
#     important for imbalanced classification datasets.
# The other options don't exist in sklearn (split_data/train/partition).


import numpy as np
from sklearn.model_selection import train_test_split

X = np.arange(20).reshape(10, 2)      # 10 samples, 2 features
y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,       # 30% of samples go to test
    random_state=42,     # reproducible split
    stratify=y,          # preserve class balance (0s and 1s) in both splits
)

print(f"X_train shape : {X_train.shape}")   # (7, 2)
print(f"X_test  shape : {X_test.shape}")    # (3, 2)
print(f"y_train       : {y_train}")
print(f"y_test        : {y_test}")

# Rule of thumb: always split BEFORE any fitting (scalers, encoders, models)
# to avoid "data leakage" from the test set contaminating training.
