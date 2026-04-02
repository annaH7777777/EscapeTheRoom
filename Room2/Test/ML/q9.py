#What does StandardScaler do?
# Standardizes to mean 0 and std 1

import numpy as np
from sklearn.preprocessing import StandardScaler
data = np.array([[1], [2], [3]])

scaler = StandardScaler()
scaled = scaler.fit_transform(data)

print(scaled)
print(scaled.mean(), scaled.std())