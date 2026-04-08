#Write a function that splits a dataset into train, validation, and test sets manually using slicing (cannot use sklearn).

import numpy as np

def train_val_test_split(X, y, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15, seed=42):
    np.random.seed(seed)
    indices = np.random.permutation(len(X))
    X, y = X[indices], y[indices]

    train_end = int(len(X) * train_ratio)
    val_end = train_end + int(len(X) * val_ratio)

    X_train, y_train = X[:train_end], y[:train_end]
    X_val, y_val = X[train_end:val_end], y[train_end:val_end]
    X_test, y_test = X[val_end:], y[val_end:]

    return X_train, X_val, X_test, y_train, y_val, y_test

X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10],
              [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]])
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])

X_train, X_val, X_test, y_train, y_val, y_test = train_val_test_split(X, y)

print(f"Train: {len(X_train)}, Val: {len(X_val)}, Test: {len(X_test)}")
print(f"Train: {len(y_train)}, Val: {len(y_val)}, Test: {len(y_test)}")
#print(f"X_train:\n{X_train}\ny_train:\n{y_train}")