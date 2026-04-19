# Q2: What is the difference between is and == in Python?
# Options:
#   - No difference
#   - is compares content, == compares identity
#   - is compares identity, == compares values
#   - Both are used for string comparison only
# Answer: is compares identity, == compares values
#
# Explanation:
#   - `==` calls __eq__ and asks: "do these two objects have equal values?"
#   - `is` asks: "are these two names pointing to the *same object in memory*?"
#     (equivalent to comparing id(a) == id(b))
# Two different list objects can hold the same values — `==` is True, `is` is
# False. Small integers and interned strings are cached by CPython, so `is`
# may *accidentally* return True for them; that's an implementation detail,
# not a guarantee. Rule of thumb: use `is` only for None, True, False, and
# sentinel singletons. Use `==` for value equality.


a = [1, 2, 3]
b = [1, 2, 3]     # different list object, same contents
c = a             # same object as a (just another name)

print(f"a == b -> {a == b}")   # True  — same values
print(f"a is b -> {a is b}")   # False — different objects
print(f"a is c -> {a is c}")   # True  — c is just another name for a

# The canonical correct use of `is`:
x = None
print(f"x is None -> {x is None}")   # True — always use `is` with None