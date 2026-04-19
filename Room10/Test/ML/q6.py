# Q6: How many outputs does train_test_split(X, y) return?
# Options:
#   - 2
#   - 3
#   - 4
#   - 1
# Answer: 4
#
# Explanation:
# For each array you pass in, train_test_split produces TWO pieces — a
# train portion and a test portion — and returns them in the order
# (train_of_arr1, test_of_arr1, train_of_arr2, test_of_arr2, ...).
# With two inputs (X and y), that's 4 outputs, unpacked in this order:
#     X_train, X_test, y_train, y_test = train_test_split(X, y)
# If you pass three arrays (e.g. X, y, sample_weight), you'll get 6 outputs.
# Gotcha: if you pass only X (no y), it returns 2 outputs — X_train, X_test.


import numpy as np
from sklearn.model_selection import train_test_split

X = np.arange(20).reshape(10, 2)
y = np.arange(10)

result = train_test_split(X, y, test_size=0.2, random_state=0)
print(f"number of outputs : {len(result)}")   # 4

X_train, X_test, y_train, y_test = result
print(f"X_train shape     : {X_train.shape}")   # (8, 2)
print(f"X_test  shape     : {X_test.shape}")    # (2, 2)
print(f"y_train shape     : {y_train.shape}")   # (8,)
print(f"y_test  shape     : {y_test.shape}")    # (2,)

# Three inputs → six outputs
weights = np.linspace(0.1, 1.0, 10)
six = train_test_split(X, y, weights, test_size=0.2, random_state=0)
print(f"\nwith 3 inputs     : {len(six)} outputs")   # 6
