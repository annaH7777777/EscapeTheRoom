# Q4 (ML): What regularization technique adds absolute value penalty?
# Answer: L1

# Penalty formulas:
# L1 (Lasso):      α * Σ|coef|      <- absolute values
# L2 (Ridge):      α * Σ(coef²)     <- squared values
# ElasticNet:      L1 + L2 combined

import numpy as np

coefs = np.array([3, -2, 0.5, -4])
alpha = 0.1

l1_penalty = alpha * np.sum(np.abs(coefs))
l2_penalty = alpha * np.sum(coefs ** 2)

print(f"Coefficients: {coefs}")
print(f"L1 penalty (absolute values): α * Σ|coef| = {l1_penalty:.2f}")
print(f"L2 penalty (squared values):  α * Σ(coef²) = {l2_penalty:.2f}")
