# Q5 (ML): What type of scaling does MinMaxScaler perform?
# Answer: Normalization (0 to 1)

import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

data = np.array([10, 20, 30, 100, 200]).reshape(-1, 1)
print(f"Original data: {data.ravel()}")

# === MinMaxScaler: scales to [0, 1] ===
print("\n=== MinMaxScaler (Normalization) ===")
mms = MinMaxScaler()
scaled = mms.fit_transform(data)
print(f"  Scaled: {scaled.ravel()}")
print(f"  Formula: (X - X_min) / (X_max - X_min)")
print(f"  Example: (30 - 10) / (200 - 10) = {(30-10)/(200-10):.4f}")
print(f"  Min -> 0, Max -> 1")

# === Manual calculation ===
print("\n=== Manual verification ===")
X_min, X_max = data.min(), data.max()
for val in data.ravel():
    manual = (val - X_min) / (X_max - X_min)
    print(f"  {val:>3} -> ({val} - {X_min}) / ({X_max} - {X_min}) = {manual:.4f}")

# === Comparison with other scalers ===
print("\n=== Comparison ===")
ss = StandardScaler().fit_transform(data)
rs = RobustScaler().fit_transform(data)
print(f"  MinMaxScaler:   {MinMaxScaler().fit_transform(data).ravel()}  (range [0,1])")
print(f"  StandardScaler: {ss.ravel().round(2)}  (mean=0, std=1)")
print(f"  RobustScaler:   {rs.ravel().round(2)}  (median=0, uses IQR)")