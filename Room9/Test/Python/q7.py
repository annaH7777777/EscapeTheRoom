# Q7: Which of the following makes a deep copy of an object?
# Options:
#   - obj.copy()
#   - deepcopy(obj)
#   - obj[:]
#   - shallow(obj)
# Answer: deepcopy(obj)  (from the copy module: copy.deepcopy)
#
# Explanation:
# - obj.copy()  → SHALLOW copy: new outer container, but nested objects
#                 are still shared with the original.
# - obj[:]      → slice copy on lists: also SHALLOW (same nested refs).
# - shallow()   → not a real built-in.
# - deepcopy(obj) from the `copy` module recursively copies every nested
#   object, so changes inside the nested structures do NOT leak into
#   the original.
# Rule of thumb: use deepcopy when objects contain mutable objects
# inside them (lists of lists, dicts of dicts, etc.).


import copy

original = [[1, 2], [3, 4]]

shallow = original.copy()          # same inner lists
deep    = copy.deepcopy(original)  # fully independent inner lists

# Mutate an inner list through the shallow copy
shallow[0].append(99)

print(f"original after shallow mutation -> {original}")  # [[1, 2, 99], [3, 4]]
print(f"shallow                         -> {shallow}")   # [[1, 2, 99], [3, 4]]
print(f"deep                            -> {deep}")      # [[1, 2], [3, 4]]  — untouched

# Identity check: are the INNER objects shared?
print(f"shallow[0] is original[0] -> {shallow[0] is original[0]}")  # True
print(f"deep[0]    is original[0] -> {deep[0] is original[0]}")     # False
