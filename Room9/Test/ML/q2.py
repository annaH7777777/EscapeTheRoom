# Q2: Which model can be used for binary classification?
# Options:
#   - kNN
#   - PCA
#   - MinMaxScaler
#   - SVC
# Answer: SVC
#
# Explanation:
# SVC (Support Vector Classifier, sklearn.svm.SVC) is a supervised
# classifier — perfect fit for binary (two-class) problems.
# Why the others do not qualify:
#   - PCA           → dimensionality-reduction technique, not a classifier.
#                     It produces new features, not class predictions.
#   - MinMaxScaler  → a preprocessing transformer that scales features
#                     into a range (e.g. 0–1). It has no .predict().
#   - kNN (KNeighborsClassifier) CAN also classify, but is a distractor
#                     in this question — SVC is the canonical classifier
#                     (its very name ends in "Classifier").
# Rule of thumb: a model usable for classification must have a .predict()
# method that returns class labels — PCA and MinMaxScaler do not.


import numpy as np
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler

X = np.array([
    [1, 1],
    [2, 1],
    [1, 2],
    [6, 7],
    [7, 7],
    [8, 6],
])
y = np.array([0, 0, 0, 1, 1, 1])   # binary labels: class 0 vs class 1

# --- SVC: the correct answer ---
svc = SVC(kernel="linear")
svc.fit(X, y)
print(f"SVC predictions : {svc.predict([[2, 2], [7, 6]]).tolist()}")  # [0, 1]
print(f"SVC accuracy    : {svc.score(X, y):.2f}")

# --- PCA: no .predict(); only transforms features ---
pca = PCA(n_components=1)
X_pca = pca.fit_transform(X)
print(f"PCA output shape: {X_pca.shape}  (features, not class labels)")
print(f"has predict?    : {hasattr(pca, 'predict')}")    # False

# --- MinMaxScaler: no .predict(); scales features to [0, 1] ---
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
print(f"Scaled range    : [{X_scaled.min()}, {X_scaled.max()}]")
print(f"has predict?    : {hasattr(scaler, 'predict')}")  # False
