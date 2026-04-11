# Q4 (ML): Which algorithm is sensitive to outliers?
# Answer: Linear Regression

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

# Clean data: y = 2*x
X_clean = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y_clean = np.array([2, 4, 6, 8, 10])

# Same data + one outlier
X_outlier = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
y_outlier = np.array([2, 4, 6, 8, 10, 100])  # 100 is an outlier (expected ~12)

# === Linear Regression: heavily affected ===
print("=== Linear Regression ===")
lr_clean = LinearRegression().fit(X_clean, y_clean)
lr_outlier = LinearRegression().fit(X_outlier, y_outlier)
print(f"  Without outlier: slope={lr_clean.coef_[0]:.2f}, intercept={lr_clean.intercept_:.2f}")
print(f"  With outlier:    slope={lr_outlier.coef_[0]:.2f}, intercept={lr_outlier.intercept_:.2f}")
print(f"  Predict X=3: clean={lr_clean.predict([[3]])[0]:.1f}, outlier={lr_outlier.predict([[3]])[0]:.1f}")

# === Decision Tree: barely affected ===
print("\n=== Decision Tree ===")
dt_clean = DecisionTreeRegressor().fit(X_clean, y_clean)
dt_outlier = DecisionTreeRegressor().fit(X_outlier, y_outlier)
print(f"  Predict X=3: clean={dt_clean.predict([[3]])[0]:.1f}, outlier={dt_outlier.predict([[3]])[0]:.1f}")
print(f"  Outlier isolated in its own leaf — doesn't affect other predictions")

# === Why Linear Regression is sensitive ===
print("\n=== Why? Squared errors ===")
print(f"  Error for outlier: (100 - 12) = 88")
print(f"  Squared error:     88^2 = {88**2}")
print(f"  This HUGE squared error pulls the entire line toward the outlier")