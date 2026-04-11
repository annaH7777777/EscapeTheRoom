# Q2 (ML): What is hyperparameter tuning?
# Answer: Finding best model settings

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

# Load data
X, y = load_iris(return_X_y=True)

# === Without tuning: just guess hyperparameters ===
print("=== Default hyperparameters ===")
model = RandomForestClassifier(random_state=42)
model.fit(X, y)
print(f"  n_estimators={model.n_estimators}, max_depth={model.max_depth}")

# === With tuning: search for the BEST hyperparameters ===
print("\n=== GridSearchCV: try all combinations ===")
param_grid = {
    "n_estimators": [10, 50, 100],
    "max_depth": [2, 5, None],
    "min_samples_split": [2, 5]
}
grid = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=3,
    scoring="accuracy"
)
grid.fit(X, y)

print(f"  Best params: {grid.best_params_}")
print(f"  Best score:  {grid.best_score_:.4f}")

# === Hyperparameters vs Parameters ===
print("\n=== Key difference ===")
print("Hyperparameters (YOU choose before training):")
print("  -> n_estimators, max_depth, learning_rate, C, kernel...")
print("Parameters (MODEL learns during training):")
print("  -> weights, biases, split thresholds...")