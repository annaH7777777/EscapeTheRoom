#Fix the function to square only numeric values.

def sum_squares(lst):
    return sum(x**2 for x in lst if isinstance(x, (int, float)))

print(sum_squares([1, 2, 'three', 4]))
