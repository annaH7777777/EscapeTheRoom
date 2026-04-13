# Q1 (ML): What is GridSearchCV used for?
# Answer: Hyperparameter tuning

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

X, y = load_iris(return_X_y=True)

# Define hyperparameter grid to search
param_grid = {
    "n_estimators": [10, 50, 100],
    "max_depth": [2, 5, None]
}

# GridSearchCV tries EVERY combination (3 x 3 = 9) with cross-validation
grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3)
grid.fit(X, y)

print(f"Best params:  {grid.best_params_}")
print(f"Best score:   {grid.best_score_:.4f}")
print(f"Total fits:   {len(grid.cv_results_['params'])} combinations × 3 folds = {len(grid.cv_results_['params']) * 3}")
