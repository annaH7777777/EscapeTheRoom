#Fix the function to return the merged dictionary.

def merge_dicts(d1, d2):
    d1.update(d2)  # fixed: update() returns None, so return dict after updating
    return d1


print(merge_dicts({'a': 1}, {'b': 2}))
