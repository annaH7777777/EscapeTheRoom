# Q5: What is returned by len(set([1, 1, 2]))?
# Options:
#   - 3
#   - 2
#   - 1
#   - Error
# Answer: 2
#
# Explanation:
# A set is an unordered collection of *unique* elements — duplicates are
# silently discarded when the set is built. So set([1, 1, 2]) becomes {1, 2},
# and len({1, 2}) is 2.
# This is the canonical one-liner for "count distinct values" in an iterable.
# Requirement: the elements must be hashable (numbers, strings, tuples work;
# lists and dicts don't — they'd raise TypeError).


data = [1, 1, 2]
unique = set(data)

print(f"list            -> {data}")           # [1, 1, 2]
print(f"set(data)       -> {unique}")         # {1, 2}
print(f"len(set(data))  -> {len(unique)}")    # 2

# Common use: count distinct values
visitors = ['alice', 'bob', 'alice', 'carol', 'bob']
print(f"distinct visitors -> {len(set(visitors))}")   # 3

# Sets also support fast membership checks
print(f"1 in set -> {1 in unique}")           # True
print(f"5 in set -> {5 in unique}")           # False
