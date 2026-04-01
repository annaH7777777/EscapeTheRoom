#Fix the code to print the sum of each row in a 2D NumPy array.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

row_sums = arr.sum(1, 1)
print("Row sums:", row_sums) #It should return Row sums: [ 6 15 ] in this case