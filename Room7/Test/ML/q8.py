# Q8 (ML): What does StandardScaler assume about features?
# Answer: Normal distribution

import numpy as np
from sklearn.preprocessing import StandardScaler

# Normal distribution: mean=50, std=10
data = np.random.normal(loc=50, scale=10, size=1000).reshape(-1, 1)

scaled = StandardScaler().fit_transform(data)

print(f"Before scaling: mean={data.mean():.2f}, std={data.std():.2f}")
print(f"After scaling:  mean={scaled.mean():.2f}, std={scaled.std():.2f}")
print(f"\nFormula: (X - mean) / std   -> mean=0, std=1")
