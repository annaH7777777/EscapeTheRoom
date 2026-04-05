#Fix the sorting function to correctly access dictionary keys without causing any error.

def sort_custom(lst, key):
    return sorted(lst, key=lambda x: x[key])  # just use x[], for dictionaries

print(sort_custom([{'a': 3}, {'a': 1}, {'a': 2}], 'a'))