# Q5 (ML): Which model is prone to high variance?
# Answer: Decision Tree

import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

# Generate noisy data
X, y = make_classification(n_samples=300, n_features=10, flip_y=0.2, random_state=42)
X_test, y_test = make_classification(n_samples=100, n_features=10, flip_y=0.2, random_state=999)

# Train each model 10 times on different random subsets, check prediction variability
tree_preds = []
logreg_preds = []
rng = np.random.RandomState(0)

for i in range(10):
    # Pick a random subset of training data
    idx = rng.choice(len(X), size=150, replace=False)

    tree = DecisionTreeClassifier(random_state=i).fit(X[idx], y[idx])
    logreg = LogisticRegression(max_iter=1000).fit(X[idx], y[idx])

    tree_preds.append(tree.predict(X_test))
    logreg_preds.append(logreg.predict(X_test))

tree_preds = np.array(tree_preds)
logreg_preds = np.array(logreg_preds)

# Variance = how much predictions change across the 10 models
tree_variance = tree_preds.std(axis=0).mean()
logreg_variance = logreg_preds.std(axis=0).mean()

print(f"Decision Tree       prediction std across 10 models: {tree_variance:.3f}")
print(f"Logistic Regression prediction std across 10 models: {logreg_variance:.3f}")
print(f"\n-> Decision Tree changes predictions MORE when training data changes = higher variance")
