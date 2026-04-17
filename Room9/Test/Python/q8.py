# Q8: What type is returned by zip()?
# Options:
#   - list
#   - tuple
#   - zip object (iterator)
#   - dict
# Answer: zip object (iterator)
#
# Explanation:
# In Python 3, zip() returns a lazy iterator of type `zip`. It does NOT
# build a list up-front — items are produced one at a time as you iterate.
# Consequences:
#   - You can iterate a zip object only ONCE; after that it is exhausted.
#   - To materialize it, wrap with list(), tuple(), or dict() — e.g.
#     list(zip(a, b)) or dict(zip(keys, values)).
# In Python 2, zip() returned a list — a common source of confusion.


names = ["Anna", "Bob", "Cara"]
ages  = [25, 30, 35]

z = zip(names, ages)
print(f"type(zip(...)) -> {type(z).__name__}")   # zip
print(f"zip object     -> {z}")                   # <zip object at 0x...>

# Iterators are exhausted after one pass — materialize to reuse:
pairs = list(zip(names, ages))
print(f"list(zip(...)) -> {pairs}")               # [('Anna', 25), ('Bob', 30), ('Cara', 35)]

# Common idiom: build a dict from two parallel lists
lookup = dict(zip(names, ages))
print(f"dict(zip(...)) -> {lookup}")              # {'Anna': 25, 'Bob': 30, 'Cara': 35}

# Demo that the iterator is one-shot
z2 = zip(names, ages)
print(f"first pass  -> {list(z2)}")               # full list of pairs
print(f"second pass -> {list(z2)}")               # []  — already exhausted
