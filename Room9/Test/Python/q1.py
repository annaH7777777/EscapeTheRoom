# Q1: Which method allows defining equality comparison for custom objects?
# Options:
#   - __eq__
#   - __cmp__
#   - __compare__
#   - equals
# Answer: __eq__
#
# Explanation:
# __eq__ is the dunder method Python calls when you use the == operator
# on two objects. By default, == compares object identity (like 'is'),
# so custom classes must override __eq__ to define value-based equality.
# __cmp__ existed in Python 2 but was removed in Python 3.
# __compare__ and equals() are not real Python magic methods.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        # Two points are equal when both coordinates match
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y


a = Point(1, 2)
b = Point(1, 2)
c = Point(3, 4)

print(f"a == b -> {a == b}")   # True  — same coordinates
print(f"a == c -> {a == c}")   # False — different coordinates
print(f"a is b -> {a is b}")   # False — different objects in memory
