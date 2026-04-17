# Q2: What is the result of all([])?
# Options:
#   - True
#   - False
#   - Error
#   - None
# Answer: True
#
# Explanation:
# all(iterable) returns True if every element is truthy — and True for an
# empty iterable by definition ("vacuous truth": there is no element that
# fails the condition, so the claim holds).
# Mnemonic: all([]) is True, any([]) is False.
# Useful when validating a list of conditions that may be empty — no items
# means nothing to violate the rule.


print(f"all([])               -> {all([])}")                # True  (empty)
print(f"all([1, 2, 3])        -> {all([1, 2, 3])}")         # True  (all truthy)
print(f"all([1, 0, 3])        -> {all([1, 0, 3])}")         # False (0 is falsy)
print(f"any([])               -> {any([])}")                # False (empty)
print(f"all([True, True])     -> {all([True, True])}")      # True
print(f"all(x > 0 for x in []) -> {all(x > 0 for x in [])}")  # True (empty generator)
