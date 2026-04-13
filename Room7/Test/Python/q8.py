# Q8: What is the result of [i for i in range(5) if i > 2]?
# Answer: [3, 4]

# The expression
result = [i for i in range(5) if i > 2]
print(f"[i for i in range(5) if i > 2] = {result}")

# Step-by-step trace
print("\n=== Step by step ===")
for i in range(5):
    passes = i > 2
    print(f"  i={i}  i>2={passes}  {'-> kept' if passes else '-> skipped'}")

# === Compare different conditions ===
print("\n=== Different conditions ===")
print(f"  i > 2   -> {[i for i in range(5) if i > 2]}   (strictly greater)")
print(f"  i >= 2  -> {[i for i in range(5) if i >= 2]}  (greater or equal)")
print(f"  i < 2   -> {[i for i in range(5) if i < 2]}      (strictly less)")
print(f"  i <= 2  -> {[i for i in range(5) if i <= 2]}  (less or equal)")

# === range reminder ===
print("\n=== range(5) ===")
print(f"  range(5) produces: {list(range(5))}")
print(f"  NOTE: range(5) gives 0..4 (NOT including 5)")

# === List comprehension syntax ===
print("\n=== Syntax ===")
print("  [ expression  for item in iterable  if condition ]")
print("       ^              ^                    ^")
print("    what to keep   loop variable      filter")
