# Q6 (ML): What does variance measure?
# Answer: Spread of data

import numpy as np

# Two datasets with the SAME mean but DIFFERENT spread
tight = np.array([9, 10, 10, 11, 10])     # clustered close to mean
spread = np.array([1, 5, 10, 15, 19])      # spread far from mean

print("=== Same mean, different variance ===")
print(f"  Tight:  {tight}  mean={tight.mean():.1f}  variance={tight.var():.2f}")
print(f"  Spread: {spread}  mean={spread.mean():.1f}  variance={spread.var():.2f}")

# === Manual calculation ===
print("\n=== Manual calculation for tight data ===")
mean = tight.mean()
print(f"  Mean = {mean}")
diffs = tight - mean
squared = diffs ** 2
print(f"  Differences from mean: {diffs}")
print(f"  Squared differences:   {squared}")
print(f"  Variance = sum / n = {squared.sum()} / {len(tight)} = {squared.sum()/len(tight):.2f}")

# === Variance vs Standard Deviation ===
print("\n=== Variance vs Standard Deviation ===")
print(f"  Variance (σ²) = {spread.var():.2f}  (squared units)")
print(f"  Std Dev  (σ)  = {spread.std():.2f}  (same units as data)")
print(f"  std = sqrt(variance) = sqrt({spread.var():.2f}) = {np.sqrt(spread.var()):.2f}")

# === In ML context: bias-variance tradeoff ===
print("\n=== In ML: Bias-Variance Tradeoff ===")
print("  High variance model -> overfits (memorizes training data)")
print("  Low variance model  -> more stable across different datasets")