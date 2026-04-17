# Q9: What is k in kNN?
# Options:
#   - Feature count
#   - Number of classes
#   - Nearest neighbors
#   - Dataset rows
# Answer: Nearest neighbors
#
# Explanation:
# In k-Nearest Neighbors, `k` is the NUMBER OF NEAREST TRAINING POINTS
# the algorithm looks at to classify a new sample. The prediction is
# the majority class among those k neighbors (for classification) or
# the average of their targets (for regression).
# In sklearn: KNeighborsClassifier(n_neighbors=k).
# Effect of k:
#   - small k (e.g. 1) → flexible / low bias, high variance → risk of overfitting
#   - large k           → smoother boundary, more bias, less variance
# NOT related to:
#   - feature count  → that is X.shape[1]
#   - class count    → that is len(np.unique(y))
#   - dataset rows   → that is X.shape[0] (often called n)


import numpy as np
from sklearn.neighbors import KNeighborsClassifier

X = np.array([
    [1, 1], [2, 1], [1, 2],
    [6, 7], [7, 7], [8, 6],
])
y = np.array([0, 0, 0, 1, 1, 1])

new_point = np.array([[3, 3]])

for k in (1, 3, 5):
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X, y)
    pred = clf.predict(new_point)[0]
    # Show WHICH neighbors were used and at what distance
    distances, indices = clf.kneighbors(new_point)
    print(
        f"k={k} | prediction={pred} | "
        f"neighbor idx={indices[0].tolist()} | "
        f"distances={distances[0].round(2).tolist()}"
    )

print(f"\nX.shape (rows, features) -> {X.shape}")     # 6 rows, 2 features
print(f"number of classes         -> {len(np.unique(y))}")   # 2
# k is independent of all three: you choose it as a hyperparameter.
