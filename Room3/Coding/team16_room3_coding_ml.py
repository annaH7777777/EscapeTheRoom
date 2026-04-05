# For Machine Learning: Using scikit-learn, create a complete machine learning pipeline that:
# loads the Iris dataset;
# applies StandardScaler for feature scaling;
# trains a Logistic Regression model;
# uses GridSearchCV to find the best value for the C parameter (regularization strength);
# prints the best hyperparameters and the model's accuracy on a test set.
# Note: GridSearchCV helps find the best model parameters automatically.

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV

# Load dataset: X = features (4 columns), y = species labels (0, 1, 2)
X, y = load_iris(return_X_y=True)
print("Full dataset shape:", X.shape, y.shape)

# Scale features to mean=0, std=1 so all features contribute equally
scaler = StandardScaler()
scaled = scaler.fit_transform(X)
print(f"scaled mean: {scaled.mean()}, std: {scaled.std()}")

# Split into 75% train / 25% test with fixed seed for reproducibility
X_train, X_test, y_train, y_test = train_test_split(scaled, y, random_state=42)
print("Train shape:", X_train.shape, "Test shape:", X_test.shape)

# Train baseline Logistic Regression with default C=1
model = LogisticRegression()
model.fit(X_train, y_train)
print("Baseline accuracy:", model.score(X_test, y_test))

# Use GridSearchCV to find the best C (regularization strength) across 5 folds
param_grid = {'C': [0.01, 0.1, 1, 10, 100]}
grid = GridSearchCV(LogisticRegression(), param_grid, cv=5)
grid.fit(X_train, y_train)

# Print best hyperparameters and final accuracy on the test set
print("Best C:", grid.best_params_)
print("Best CV score:", grid.best_score_)
print("Test accuracy:", grid.score(X_test, y_test))