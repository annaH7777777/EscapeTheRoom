# Q3: Which built-in function checks if all elements in an iterable are true?
# Options:
#   - any()
#   - all()
#   - bool()
#   - check()
# Answer: all()
#
# Explanation:
# all(iterable) returns True if *every* element is truthy (or the iterable
# is empty — vacuous truth). It short-circuits: as soon as it finds a
# falsy value, it stops and returns False.
# any(iterable) is the counterpart: True if *at least one* element is truthy.
# bool(x) converts a single value to True/False — it doesn't iterate.
# check() is not a built-in at all.
# Mnemonic: all = AND-reduce, any = OR-reduce.


print(f"all([1, 2, 3])      -> {all([1, 2, 3])}")       # True  — all truthy
print(f"all([1, 0, 3])      -> {all([1, 0, 3])}")       # False — 0 is falsy
print(f"all([])             -> {all([])}")              # True  — empty = vacuous truth
print(f"any([0, 0, 1])      -> {any([0, 0, 1])}")       # True  — one truthy value
print(f"any([])             -> {any([])}")              # False — empty

# Typical use: validate a list of conditions in one line
ages = [18, 21, 30, 25]
print(f"all adults? -> {all(age >= 18 for age in ages)}")   # True
print(f"any minor?  -> {any(age < 18 for age in ages)}")    # False
