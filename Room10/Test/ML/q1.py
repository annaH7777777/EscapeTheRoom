# Q1: What is the main difference between supervised and unsupervised learning?
# Options:
#   - Unsupervised is for images
#   - Supervised uses labeled data
#   - Supervised uses neural networks
#   - Unsupervised uses testing data only
# Answer: Supervised uses labeled data
#
# Explanation:
# The defining difference is whether the training data has *labels* (known
# correct answers):
#   - Supervised learning:   X (features) + y (labels). The model learns
#     the mapping X -> y. Tasks: classification, regression.
#   - Unsupervised learning: X only, no y. The model finds structure on its
#     own. Tasks: clustering (KMeans), dimensionality reduction (PCA),
#     anomaly detection.
# The other options are wrong:
#   - "Unsupervised is for images"       — both paradigms handle images.
#   - "Supervised uses neural networks"  — not exclusive; SVM, trees,
#                                          logistic regression are also
#                                          supervised and non-neural.
#   - "Unsupervised uses testing data only" — unsupervised uses training
#                                          data (without labels), not
#                                          a "testing set".


import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans

X = np.array([
    [1, 1], [2, 1], [1, 2],
    [6, 7], [7, 7], [8, 6],
])
y = np.array([0, 0, 0, 1, 1, 1])      # <-- labels present: SUPERVISED

# Supervised: model is told which points belong to which class
sup = LogisticRegression().fit(X, y)
print(f"supervised preds  : {sup.predict([[2, 2], [7, 6]]).tolist()}")  # [0, 1]

# Unsupervised: same X, but NO labels are passed to .fit()
uns = KMeans(n_clusters=2, n_init=10, random_state=0)
uns.fit(X)
print(f"unsupervised lbls : {uns.labels_.tolist()}")   # KMeans invented 2 groups
print(f"unsupervised preds: {uns.predict([[2, 2], [7, 6]]).tolist()}")
