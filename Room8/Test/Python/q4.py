# Q4: How do you check if an object has a specific attribute?
# Options:
#   - has_attr()
#   - obj.has()
#   - hasattr(obj, 'attr')
#   - check_attr()
# Answer: hasattr(obj, 'attr')
#
# Explanation:
# hasattr(obj, name) is a built-in function that returns True if
# the object has an attribute with the given name, otherwise False.
# Internally it tries getattr(obj, name) and catches AttributeError.
# The other options are not real Python built-ins.


class Car:
    def __init__(self, brand):
        self.brand = brand
        self.wheels = 4


c = Car("Toyota")

print(f"hasattr(c, 'brand')  -> {hasattr(c, 'brand')}")   # True
print(f"hasattr(c, 'wheels') -> {hasattr(c, 'wheels')}")  # True
print(f"hasattr(c, 'color')  -> {hasattr(c, 'color')}")   # False

# Common pattern: check before accessing to avoid AttributeError
if hasattr(c, "color"):
    print(f"Color: {c.color}")
else:
    print("No 'color' attribute — using default 'unknown'")

# Related built-ins:
#   getattr(obj, name, default) -> value or default if missing
#   setattr(obj, name, value)   -> sets the attribute
#   delattr(obj, name)          -> deletes the attribute
print(f"getattr(c, 'color', 'unknown') -> {getattr(c, 'color', 'unknown')}")
