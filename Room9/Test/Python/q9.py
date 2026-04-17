# Q9: What does `del` do to a variable?
# Options:
#   - Clears its memory
#   - Removes its reference
#   - Converts it to None
#   - Sends it to GC
# Answer: Removes its reference
#
# Explanation:
# `del x` unbinds the NAME `x` from its current object — it removes the
# reference, not the object itself. The object is only freed when the
# garbage collector sees that NO references to it remain.
# Consequences:
#   - After `del x`, using `x` raises NameError (the name is gone).
#   - The object may still live on if something else refers to it.
#   - `x = None` keeps the name but rebinds it to None — different from del.


# Case 1: two names pointing at the same object
a = [1, 2, 3]
b = a                   # 'a' and 'b' share the same list object
del a                   # only the NAME 'a' is removed; the list survives via 'b'

print(f"b after del a -> {b}")         # [1, 2, 3] — object still alive
try:
    print(a)                            # NameError — 'a' no longer exists
except NameError as e:
    print(f"accessing a  -> NameError: {e}")

# Case 2: compare with `x = None` (rebinding, not deleting)
c = [10, 20]
c = None
print(f"c after = None -> {c}")        # None  — name still exists, now bound to None

# Case 3: del also works on dict keys, list indices, and attributes
d = {"x": 1, "y": 2}
del d["x"]
print(f"dict after del d['x'] -> {d}") # {'y': 2}
