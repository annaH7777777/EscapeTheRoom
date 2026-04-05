#What does StandardScaler do?
#Scales data using mean=0 and std=1

from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[10], [20], [30], [40], [50]])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(X_scaled)
print(X_scaled.mean())  # → 0.0
print(X_scaled.std())   # → 1.0