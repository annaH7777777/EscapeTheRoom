# Q7: Which method is used to define object string output for developers (debug)?
# Options:
#   - __str__()
#   - __repr__()
#   - __print__()
#   - toString()
# Answer: __repr__()
#
# Explanation:
# Python has two string-conversion dunders — they serve different audiences:
#   - __repr__(self): for *developers*. Should be unambiguous and, ideally,
#     return a string that could recreate the object (e.g. "Point(1, 2)").
#     This is what you see in the REPL, in debuggers, and inside containers
#     like lists ([Point(1,2), Point(3,4)] uses __repr__ for each item).
#   - __str__(self): for *users*. Called by print() and str(). Should be
#     human-friendly. If __str__ is missing, Python falls back to __repr__.
# So: always define __repr__, define __str__ only if you want a separate
# user-facing format.
# __print__ is not a real dunder. toString() is Java/JS syntax.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # developer view — unambiguous, ideally "eval-able"
        return f"Point(x={self.x}, y={self.y})"

    def __str__(self):
        # user-facing — friendly format
        return f"({self.x}, {self.y})"


p = Point(3, 4)

print(f"print(p)    -> {p}")           # uses __str__  -> (3, 4)
print(f"repr(p)     -> {repr(p)}")     # uses __repr__ -> Point(x=3, y=4)
print(f"in a list   -> {[p, p]}")      # list uses __repr__ per element

# Without __str__, print() falls back to __repr__
class Tag:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Tag({self.name!r})"


t = Tag("urgent")
print(f"no __str__  -> {t}")           # falls back to __repr__
