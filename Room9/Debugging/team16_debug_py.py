#Fix the function to properly reverse a dictionary and handle cases where multiple keys may share a value.

def reverse_dict(d):
    res = {}
    for k, v in d.items():
       # Instead of res[v] = k we write:
        res.setdefault(v, []).append(k)
    return res
    
print(reverse_dict({'a': 1, 'b': 1, 'c': 2}))
