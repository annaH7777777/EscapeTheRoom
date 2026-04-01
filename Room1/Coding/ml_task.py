#For Machine Learning: Write a function diagonal_product(arr: np.ndarray) -> int that returns the product of the diagonal of a 3x3 NumPy array.
#Example: [[1,2,3],[4,5,6],[7,8,9]] returns 45.
import numpy as np

def diagonal_product(arr: np.ndarray):
    np_arr = np.array(arr)
    product = np.prod(np_arr.diagonal())
    return product

if __name__ == '__main__':
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    try:
        result = diagonal_product(arr)
        print(f"Diagonal product is: {result}")
    except ValueError:
        print("Error: Please enter a valid array.")
