# Q4: What will [i for i in range(5) if i % 2 == 1] return?
# Options:
#   - [0, 2, 4]
#   - [1, 3]
#   - [2, 4]
#   - [1, 2, 3, 4]
# Answer: [1, 3]
#
# Explanation:
# range(5) produces 0, 1, 2, 3, 4 (stop value 5 is NOT included).
# The filter `if i % 2 == 1` keeps only numbers whose remainder when
# divided by 2 is 1 — i.e. odd numbers.
# From {0, 1, 2, 3, 4} the odd ones are 1 and 3, giving [1, 3].
# Trap: `i % 2 == 0` would give the evens [0, 2, 4].


odds = [i for i in range(5) if i % 2 == 1]
evens = [i for i in range(5) if i % 2 == 0]
all_vals = list(range(5))

print(f"range(5) as list            -> {all_vals}")   # [0, 1, 2, 3, 4]
print(f"[i for i in range(5) if i%2==1] -> {odds}")   # [1, 3]
print(f"[i for i in range(5) if i%2==0] -> {evens}")  # [0, 2, 4]
