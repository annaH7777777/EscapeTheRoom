# Q5: What does __call__ allow an object to do?
# Options:
#   - Be used in print()
#   - Be callable like a function
#   - Be added to a string
#   - Raise an exception
# Answer: Be callable like a function
#
# Explanation:
# When a class defines __call__, its instances become *callable* —
# you can use `obj(...)` just like `func(...)`. Python invokes
# obj.__call__(...) under the hood.
# This is how decorator classes, function-like stateful objects,
# and things like torch.nn.Module or sklearn estimators work.
# Related dunders — do NOT confuse:
#   - __str__  / __repr__ → used by print()
#   - __add__             → used by `+` (string/number addition)


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        # Instance behaves like a function: Multiplier(3)(10) -> 30
        return x * self.factor


double = Multiplier(2)
triple = Multiplier(3)

print(f"callable(double) -> {callable(double)}")   # True — has __call__
print(f"double(10)       -> {double(10)}")         # 20
print(f"triple(10)       -> {triple(10)}")         # 30

# Useful pattern: pass a callable object where a function is expected
nums = [1, 2, 3, 4]
print(f"map(double, nums) -> {list(map(double, nums))}")  # [2, 4, 6, 8]
