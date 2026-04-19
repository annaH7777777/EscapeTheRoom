# Q4: What does zip(['a', 'b'], [1, 2]) return?
# Options:
#   - A dictionary
#   - An iterator of pairs: [('a', 1), ('b', 2)]
#   - A tuple
#   - A single string
# Answer: An iterator of pairs: [('a', 1), ('b', 2)]
#
# Explanation:
# zip() takes two or more iterables and produces an *iterator* that yields
# tuples pairing items by position: the i-th tuple contains the i-th item
# from each input. It's lazy — nothing is computed until you iterate over
# it (or convert it to a list/dict/etc.).
# If inputs have different lengths, zip stops at the shortest one (use
# itertools.zip_longest to pad instead).
# To get a dict, wrap it: dict(zip(keys, values)).
# Important gotcha: a zip object is *single-use* — once consumed, it's empty.


z = zip(['a', 'b'], [1, 2])
print(f"type(z) -> {type(z).__name__}")     # zip  (an iterator, not a list)
print(f"list(z) -> {list(z)}")              # [('a', 1), ('b', 2)]

# Common idioms:
keys = ['name', 'age', 'city']
vals = ['Anna', 30, 'Yerevan']
print(f"as dict -> {dict(zip(keys, vals))}")   # {'name': 'Anna', 'age': 30, 'city': 'Yerevan'}

# Unequal lengths — zip stops at the shortest input
print(f"uneven  -> {list(zip([1, 2, 3, 4], ['a', 'b']))}")   # [(1, 'a'), (2, 'b')]

# Unzip pattern: zip(*pairs) inverts a list of tuples
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
print(f"unzipped -> letters={letters}, numbers={numbers}")   # ('a','b','c'), (1,2,3)
