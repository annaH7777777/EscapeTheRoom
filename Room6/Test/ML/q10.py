# Q10 (ML): Which regularization is used to shrink coefficients toward zero?
# Answer: Lasso (L1 regularization)

import numpy as np
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet

# Data with 5 features, but only 2 actually matter
np.random.seed(42)
X = np.random.randn(100, 5)
y = 3 * X[:, 0] + 5 * X[:, 1] + np.random.normal(0, 0.5, 100)  # only features 0 and 1 matter

# === No regularization ===
lr = LinearRegression().fit(X, y)
print("=== No regularization (Linear Regression) ===")
print(f"  Coefficients: {np.round(lr.coef_, 3)}")
print(f"  All features get non-zero coefficients")

# === Lasso (L1): shrinks to EXACTLY zero ===
lasso = Lasso(alpha=0.5).fit(X, y)
print("\n=== Lasso (L1) — shrinks coefficients TO zero ===")
print(f"  Coefficients: {np.round(lasso.coef_, 3)}")
print(f"  Zeros: {sum(lasso.coef_ == 0)} features eliminated!")
print(f"  -> Acts as FEATURE SELECTION")

# === Ridge (L2): shrinks but never to zero ===
ridge = Ridge(alpha=0.5).fit(X, y)
print("\n=== Ridge (L2) — shrinks but never exactly zero ===")
print(f"  Coefficients: {np.round(ridge.coef_, 3)}")
print(f"  Zeros: {sum(ridge.coef_ == 0)} (none are exactly zero)")

# === ElasticNet: mix of both ===
enet = ElasticNet(alpha=0.5, l1_ratio=0.5).fit(X, y)
print("\n=== ElasticNet (L1 + L2 combined) ===")
print(f"  Coefficients: {np.round(enet.coef_, 3)}")

# === Summary ===
print("\n=== Summary ===")
print("  Lasso (L1):   penalty = α * Σ|coef|      -> coefficients become ZERO")
print("  Ridge (L2):   penalty = α * Σ(coef²)     -> coefficients become SMALL")
print("  ElasticNet:   penalty = L1 + L2 combined  -> mix of both")
