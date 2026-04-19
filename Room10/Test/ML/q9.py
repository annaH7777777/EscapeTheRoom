# Q9: Which model type does KNeighborsClassifier belong to?
# Options:
#   - Regression
#   - Classification
#   - Normalization
#   - Encoding
# Answer: Classification
#
# Explanation:
# The name tells the story: "Classifier" at the end means it predicts
# discrete class labels. It's the classification variant of the k-nearest-
# neighbors algorithm:
#   1. For a new point, find the k closest training points (by distance).
#   2. Take a majority vote of their labels — that's the prediction.
# Its sibling for numeric targets is KNeighborsRegressor (averages the
# neighbors' values instead of voting).
# Characteristics of kNN:
#   - Lazy / instance-based: no real "training" — it just stores the data
#     and does all the work at predict time.
#   - Very sensitive to feature scale → almost always use StandardScaler
#     before fitting.
#   - Choice of k is a bias/variance knob: small k = noisy, large k = blurred.
# "Normalization" and "Encoding" are preprocessing steps, not model types.


import numpy as np
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor

X = np.array([[1, 1], [2, 1], [1, 2], [6, 7], [7, 7], [8, 6]])
y_class = np.array([0, 0, 0, 1, 1, 1])       # discrete labels -> Classification
y_reg   = np.array([1.0, 1.5, 1.2, 6.5, 7.0, 7.3])   # numeric -> Regression

# Classification
clf = KNeighborsClassifier(n_neighbors=3).fit(X, y_class)
print(f"classifier preds : {clf.predict([[2, 2], [7, 6]]).tolist()}")   # [0, 1]
print(f"classes_         : {clf.classes_}")
print(f"accuracy         : {clf.score(X, y_class):.2f}")

# Sibling: regression version of the same algorithm
reg = KNeighborsRegressor(n_neighbors=3).fit(X, y_reg)
print(f"\nregressor preds  : {reg.predict([[2, 2], [7, 6]]).round(2)}")
