# Q1: What is supervised learning?
# Options:
#   - Training without labels
#   - Training with labels
#   - Visualization only
#   - Clustering only
# Answer: Training with labels
#
# Explanation:
# Supervised learning trains a model on data where each sample has a
# known target/label (y). The model learns the mapping X -> y so it can
# predict the label for new, unseen inputs.
#   - "Training without labels"  → unsupervised learning (e.g. clustering, PCA).
#   - "Visualization only"       → exploratory data analysis, not learning.
#   - "Clustering only"          → a specific unsupervised technique.
# Typical supervised tasks:
#   - classification → label is a category (spam / not spam)
#   - regression     → label is a number (house price)


import numpy as np
from sklearn.linear_model import LogisticRegression

# Features (X): inputs the model sees
X = np.array([
    [1, 1],
    [2, 1],
    [1, 2],
    [6, 7],
    [7, 7],
    [8, 6],
])

# Labels (y): the CORRECT answers — this is what makes the task "supervised"
y = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)              # learns X -> y because y is provided

predictions = model.predict([[2, 2], [7, 6]])
print(f"X shape        : {X.shape}")
print(f"Labels (y)     : {y}")
print(f"Predictions    : {predictions.tolist()}")   # expected roughly [0, 1]
print(f"Train accuracy : {model.score(X, y):.2f}")
