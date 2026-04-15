# Q3: Which function splits data in sklearn?
# Options:
#   - data_split()
#   - train_test_split()
#   - split_data()
#   - divide_data()
# Answer: train_test_split()
#
# Explanation:
# sklearn.model_selection.train_test_split(X, y, test_size=..., random_state=...)
# randomly splits the arrays into a training set and a test set.
# Key parameters:
#   - test_size   : fraction (0.2 -> 20% test) or absolute count
#   - random_state: seed for reproducibility
#   - stratify=y  : keep class proportions the same in train and test
# The other options are not real sklearn functions.


import numpy as np
from sklearn.model_selection import train_test_split

# 10 samples, 2 features each
X = np.arange(20).reshape(10, 2)
y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,          # 30% of data goes to test set
    random_state=42,        # reproducible shuffle
    stratify=y,             # keep class balance in both splits
)

print(f"X shape:       {X.shape}")
print(f"X_train shape: {X_train.shape}   y_train: {y_train}")
print(f"X_test  shape: {X_test.shape}   y_test:  {y_test}")

# Typical ML workflow:
#   1. train_test_split  -> hold out test data
#   2. model.fit(X_train, y_train)
#   3. model.score(X_test, y_test)  -> unbiased performance estimate
