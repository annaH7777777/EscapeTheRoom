#Write a function that calculates the Euclidean distance between two NumPy vectors.
import numpy as np

def euclidean_distance(arr1: np.ndarray, arr2: np.ndarray):
    if arr1.shape != arr2.shape:
        raise ValueError("Input vectors must have the same shape.")
    euc_distance = np.linalg.norm(arr1 - arr2)
    return euc_distance

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
distance = euclidean_distance(a, b)
print("Euclidean distance:", distance)  # Should print approximately 5.196