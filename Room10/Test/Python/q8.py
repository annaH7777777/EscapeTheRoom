# Q8: What is a typical use for list comprehension?
# Options:
#   - Import modules
#   - Build lists concisely
#   - Create classes
#   - Error handling
# Answer: Build lists concisely
#
# Explanation:
# A list comprehension is a compact expression for building a new list from
# an iterable, optionally with a filter:
#     [expression for item in iterable if condition]
# It replaces the classic three-line pattern:
#     result = []
#     for item in iterable:
#         if condition:
#             result.append(expression)
# Benefits: fewer lines, more readable for simple transforms, and slightly
# faster than an equivalent for-loop + append (no attribute lookup per step).
# Caveat: if the body gets complex (nested ifs, multiple for-clauses), a
# plain loop is more readable — don't force everything into a one-liner.
# Related: set comprehensions {x for x in ...} and dict comprehensions
# {k: v for ... in ...} share the same syntax.


# 1. Simple transform: squares of 0..5
squares = [x * x for x in range(6)]
print(f"squares        -> {squares}")          # [0, 1, 4, 9, 16, 25]

# 2. Filter: only even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(f"evens          -> {evens}")            # [0, 2, 4, 6, 8]

# 3. Transform + filter: squares of odd numbers
odd_sq = [x * x for x in range(10) if x % 2 == 1]
print(f"odd squares    -> {odd_sq}")           # [1, 9, 25, 49, 81]

# 4. From strings: uppercase a list of words
words = ["apple", "banana", "cherry"]
upper = [w.upper() for w in words]
print(f"upper          -> {upper}")            # ['APPLE', 'BANANA', 'CHERRY']

# 5. Nested loops: flatten a matrix
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [n for row in matrix for n in row]
print(f"flat           -> {flat}")             # [1, 2, 3, 4, 5, 6]

# Related siblings:
print(f"set comp       -> { {x % 3 for x in range(10)} }")
print(f"dict comp      -> { {w: len(w) for w in words} }")
