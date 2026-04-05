#Which of the following is true about is vs ==?
#"is" compares identity, "==" compares values
a = [1, 2, 3]
b = [1, 2, 3]

print(f"a == b: {a == b}")  # → True  (same value)
print(f"a is b: {a is b}")  # → False (different objects in memory)

c = a
print(f"a is c: {a is c}")  # → True  (same object!)

x = 1000
y = 1000
print(f"x == y: {x == y}")  # → True
print(f"x is y: {x is y}")  # → False (usually!)
