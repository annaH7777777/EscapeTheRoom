# Q9: What is the output of [i for i in range(5) if i%2]?
# Answer: [1, 3]

# The expression
result = [i for i in range(5) if i % 2]
print(f"[i for i in range(5) if i%2] = {result}")

# Step-by-step breakdown
print("\n=== Step by step ===")
for i in range(5):
    remainder = i % 2
    truthy = bool(remainder)
    print(f"i={i}  i%2={remainder}  truthy={truthy}  {'-> included' if truthy else '-> skipped'}")

# Key concept: 0 is falsy, non-zero is truthy
print("\n=== Truthiness in Python ===")
print(f"bool(0) = {bool(0)}")   # False
print(f"bool(1) = {bool(1)}")   # True

# Comparison: getting EVEN numbers instead
print(f"\n=== Opposite: even numbers ===")
evens = [i for i in range(5) if i % 2 == 0]
print(f"[i for i in range(5) if i%2 == 0] = {evens}")