#What is the default scaler in StandardScaler()?
#0 mean, unit variance

from sklearn.preprocessing import StandardScaler
import numpy as np

data = np.array([[10], [20], [30]])
scaler = StandardScaler()
scaled = scaler.fit_transform(data)
print(f"Scaled data: {scaled}")
print(f"Mean: {scaled.mean():.2f}")  # → 0.00
print(f"Std: {scaled.std():.2f}")    # → 1.00