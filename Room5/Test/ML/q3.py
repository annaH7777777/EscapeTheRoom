#What is feature scaling?
#Normalizing feature values

from sklearn.preprocessing import StandardScaler
import numpy as np

data = np.array([[1000, 2], [2000, 4], [3000, 6]])
scaler = StandardScaler()
scaled = scaler.fit_transform(data)

print(f"Before:\n{data}")
print(f"After:\n{scaled}")
# All features now have mean=0 and std=1