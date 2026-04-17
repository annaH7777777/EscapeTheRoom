# Q10: Which of the following is immutable?
# Options:
#   - list
#   - dict
#   - set
#   - tuple
# Answer: tuple
#
# Explanation:
# "Immutable" means the object cannot be changed after creation.
#   - tuple    → IMMUTABLE (no append/remove/item assignment).
#   - list     → mutable (supports append, pop, item assignment).
#   - dict     → mutable (keys/values can be added, removed, updated).
#   - set      → mutable (add/remove). For an immutable set, use `frozenset`.
# Practical consequence: only immutable (hashable) objects can be used as
# dict keys or set elements — that's why you can key a dict by a tuple
# but not by a list.


# --- tuple: cannot be changed ---
t = (1, 2, 3)
print(f"tuple  -> {t}")
try:
    t[0] = 99                 # TypeError
except TypeError as e:
    print(f"tuple assign -> TypeError: {e}")

# --- list: mutable ---
L = [1, 2, 3]
L[0] = 99
L.append(4)
print(f"list after mutation   -> {L}")

# --- dict: mutable ---
d = {"a": 1}
d["b"] = 2
print(f"dict after mutation   -> {d}")

# --- set: mutable; use frozenset for an immutable variant ---
s = {1, 2, 3}
s.add(4)
print(f"set after mutation    -> {s}")
fs = frozenset([1, 2, 3])
print(f"frozenset             -> {fs}  (no .add available)")

# Only immutable (hashable) objects can be dict keys / set members
lookup = {(0, 0): "origin", (1, 2): "point"}
print(f"dict keyed by tuples  -> {lookup}")
try:
    bad = {[1, 2]: "nope"}   # TypeError: unhashable type: 'list'
except TypeError as e:
    print(f"dict keyed by list    -> TypeError: {e}")
