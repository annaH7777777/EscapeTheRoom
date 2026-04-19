# Q10: What is the result of None == False?
# Options:
#   - True
#   - False
#   - Error
#   - None
# Answer: False
#
# Explanation:
# None and False are two distinct singleton objects. `==` compares values,
# and Python does NOT treat them as equal — None is not False, it's the
# absence of a value.
# The confusion comes from *truthiness*: both None and False are "falsy"
# in a boolean context, so `bool(None)` and `bool(False)` are both False,
# and `if None:` behaves the same as `if False:`. But that's implicit
# conversion to bool — the objects themselves are not equal.
# Rule: use `is None` to check for None, and `if not x:` only when you
# actually want to treat None, False, 0, '', [] all the same.


print(f"None == False        -> {None == False}")        # False — distinct values
print(f"None == None         -> {None == None}")         # True
print(f"None is None         -> {None is None}")         # True (preferred form)
print(f"False == 0           -> {False == 0}")           # True! bool is a subclass of int
print(f"True == 1            -> {True == 1}")            # True! same reason

# Truthiness vs equality — both are falsy, but not equal
print(f"bool(None)           -> {bool(None)}")           # False
print(f"bool(False)          -> {bool(False)}")          # False

# Common trap: "if not value" treats None and False the same
for val in [None, False, 0, "", [], "ok"]:
    print(f"  not {val!r:<7} -> {not val}")

# Use `is None` when you specifically want to test for None:
x = None
print(f"x is None            -> {x is None}")            # True — the right check
