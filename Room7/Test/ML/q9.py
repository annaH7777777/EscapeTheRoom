# Q9 (ML): What happens if you over-tune hyperparameters?
# Answer: Overfit

# Over-tuning = trying too many hyperparameter combinations on the same
# validation set. Eventually you find one that "works" by chance — but it's
# memorizing validation-set quirks, not learning real patterns.
#
# Result: great validation score, poor test/real-world score.

from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=300, n_features=20, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=42)

# Very specific, over-tuned hyperparameters (found by trying 1000s)
over_tuned = DecisionTreeClassifier(max_depth=None, min_samples_split=2, random_state=42)
over_tuned.fit(X_train, y_train)

# Reasonably tuned
reasonable = DecisionTreeClassifier(max_depth=5, min_samples_split=10, random_state=42)
reasonable.fit(X_train, y_train)

print(f"Over-tuned:  train={over_tuned.score(X_train, y_train):.2f}  val={over_tuned.score(X_val, y_val):.2f}")
print(f"Reasonable:  train={reasonable.score(X_train, y_train):.2f}  val={reasonable.score(X_val, y_val):.2f}")
print("\n-> Over-tuned model has perfect train score but worse validation = overfit")
