# Q7: Which exception is raised when accessing missing dict keys?
# Answer: KeyError

d = {"name": "Anna", "age": 25}

# === KeyError when key is missing ===
print("=== Accessing missing key with d[key] ===")
try:
    value = d["country"]
except KeyError as e:
    print(f"  KeyError: {e}")

# === Safe alternatives (no error) ===
print("\n=== Safe ways to access keys ===")

# 1. .get() — returns None (or default) if key is missing
print(f"  d.get('country')         = {d.get('country')}")
print(f"  d.get('country', 'USA')  = {d.get('country', 'USA')}")

# 2. Check with 'in' before accessing
if "country" in d:
    print(d["country"])
else:
    print(f"  'country' in d  -> False, so didn't access")

# 3. try/except
try:
    print(d["country"])
except KeyError:
    print(f"  try/except  -> caught KeyError")

# === Different errors for different situations ===
print("\n=== Related exceptions ===")

# ValueError: correct type, wrong value
try:
    int("not_a_number")
except ValueError as e:
    print(f"  ValueError (wrong value):      {e}")

# TypeError: wrong type
try:
    "a" + 1
except TypeError as e:
    print(f"  TypeError (wrong type):        {e}")

# AttributeError: missing attribute on object
try:
    "hello".missing_method()
except AttributeError as e:
    print(f"  AttributeError (no attribute): {e}")

# KeyError: missing dict key
try:
    d["country"]
except KeyError as e:
    print(f"  KeyError (missing dict key):   {e}")

# Bonus: IndexError for lists
try:
    [1, 2, 3][99]
except IndexError as e:
    print(f"  IndexError (missing list idx): {e}")
