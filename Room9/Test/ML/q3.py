# Q3: What does train_test_split return?
# Options:
#   - 2 outputs
#   - 3 outputs
#   - 4 outputs
#   - 1 output
# Answer: 4 outputs
#
# Explanation:
# sklearn.model_selection.train_test_split splits EACH array you pass
# into TWO parts (train and test). With the typical call
#   train_test_split(X, y)
# you get 4 outputs, in this exact order:
#   X_train, X_test, y_train, y_test
# General rule: if you pass N arrays, it returns 2*N arrays.
# Useful parameters:
#   - test_size   → fraction of data held out (default 0.25)
#   - random_state→ seed for reproducible splits
#   - stratify=y  → keep the class ratio the same in train and test


import numpy as np
from sklearn.model_selection import train_test_split

X = np.arange(20).reshape(10, 2)         # 10 samples, 2 features
y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

# The canonical call: pass X and y → get 4 outputs back
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y,
)

print(f"X_train shape: {X_train.shape}")   # 7 rows (70%)
print(f"X_test  shape: {X_test.shape}")    # 3 rows (30%)
print(f"y_train      : {y_train}")
print(f"y_test       : {y_test}")

# Proof that it really is a 4-tuple
result = train_test_split(X, y, test_size=0.3, random_state=42)
print(f"len(result)  : {len(result)}")     # 4

# If you pass 3 arrays, you get 6 outputs (2 per array)
extra = np.arange(10)
a_tr, a_te, b_tr, b_te, c_tr, c_te = train_test_split(X, y, extra, test_size=0.3, random_state=42)
print(f"splitting 3 arrays -> 6 outputs (2 per input)")
