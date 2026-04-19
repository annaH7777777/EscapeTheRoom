# Q9: What will sorted([3, 1, 2]) return?
# Options:
#   - (1, 2, 3)
#   - [1, 2, 3]
#   - [3, 1, 2]
#   - None
# Answer: [1, 2, 3]
#
# Explanation:
# sorted(iterable) returns a *new list* with the items in ascending order.
# The original iterable is NOT modified — this is the key difference from
# list.sort(), which sorts in place and returns None.
# sorted() works with any iterable (list, tuple, set, generator) and always
# returns a list — even if the input is a tuple.
# Useful options:
#   - reverse=True        — descending order
#   - key=<function>      — sort by a computed key (e.g. key=len, key=str.lower)


original = [3, 1, 2]
result = sorted(original)

print(f"sorted([3,1,2]) -> {result}")          # [1, 2, 3] — new list
print(f"original stays  -> {original}")        # [3, 1, 2] — unchanged

# Contrast with .sort() — in-place, returns None
copy = [3, 1, 2]
ret = copy.sort()
print(f"list.sort() returns -> {ret}")         # None  (classic gotcha!)
print(f"list now            -> {copy}")        # [1, 2, 3]

# sorted() accepts any iterable — always returns a list
print(f"sorted(tuple)   -> {sorted((3, 1, 2))}")            # [1, 2, 3]  (list, not tuple)
print(f"sorted(set)     -> {sorted({'b', 'a', 'c'})}")      # ['a','b','c']

# Useful options:
words = ["banana", "fig", "apple"]
print(f"by length       -> {sorted(words, key=len)}")          # ['fig','apple','banana']
print(f"descending      -> {sorted([3, 1, 2], reverse=True)}") # [3, 2, 1]
