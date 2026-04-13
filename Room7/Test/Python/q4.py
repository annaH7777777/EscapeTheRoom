# Q4: What happens if you try to modify a tuple?
# Answer: It errors

# Tuples are IMMUTABLE — cannot be changed after creation
t = (1, 2, 3)
print(f"Original tuple: {t}")

# === Try to modify: TypeError ===
print("\n=== Trying to modify a tuple ===")
try:
    t[0] = 99
except TypeError as e:
    print(f"  Error: {e}")

# === Try to delete an item: also TypeError ===
print("\n=== Trying to delete an item ===")
try:
    del t[0]
except TypeError as e:
    print(f"  Error: {e}")

# === Workaround: create a NEW tuple (you do it manually) ===
print("\n=== Workaround: build a new tuple ===")
t_new = (99,) + t[1:]
print(f"  Original: {t}")
print(f"  New:      {t_new}")
print(f"  Same object? {t is t_new}")

# === Convert to list to modify, then back ===
print("\n=== Convert to list, modify, convert back ===")
as_list = list(t)
as_list[0] = 99
t_modified = tuple(as_list)
print(f"  Result: {t_modified}")

# === Tuple vs List ===
print("\n=== Tuple vs List ===")
lst = [1, 2, 3]
lst[0] = 99    # works fine
print(f"  List modification works: {lst}")

# === WARNING: mutable objects INSIDE a tuple can still change ===
print("\n=== Edge case: mutable items inside tuple ===")
t = ([1, 2], [3, 4])
t[0].append(99)  # This WORKS because we modify the inner list, not the tuple
print(f"  Tuple with mutable list inside: {t}")
print(f"  (The tuple itself didn't change — the list inside it did)")
