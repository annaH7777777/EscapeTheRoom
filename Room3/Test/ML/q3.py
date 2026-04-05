#Which function is commonly used as an activation in neural nets?
# ReLU

def relu(x):
    return max(0, x)

# Examples:
print(relu(-5))  # → 0
print(relu(0))   # → 0
print(relu(3))   # → 3
print(relu(7))   # → 7
print(relu(7))   # → 7