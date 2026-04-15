# Q6: What is the output of [x for x in [None, 0, 1] if x]?
# Options:
#   - [None, 0, 1]
#   - [0, 1]
#   - [1]
#   - []
# Answer: [1]
#
# Explanation:
# The `if x` filter keeps only elements that are truthy.
# In Python, the following values are FALSY:
#   None, 0, 0.0, "", [], {}, set(), False
# So from [None, 0, 1]:
#   - None -> falsy -> skipped
#   - 0    -> falsy -> skipped
#   - 1    -> truthy -> kept
# Result: [1]


data = [None, 0, 1]
result = [x for x in data if x]
print(f"[x for x in {data} if x] = {result}")

# Quick truthiness check for each element
for x in data:
    print(f"  bool({x!r:>5}) = {bool(x)}")

# If you want to keep zeros but drop only None, be explicit:
result_keep_zero = [x for x in data if x is not None]
print(f"Keeping zero: {result_keep_zero}")   # [0, 1]
