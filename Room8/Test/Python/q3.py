# Q3: What does __repr__ typically return?
# Options:
#   - A pretty string
#   - A formal string for debugging
#   - Class name
#   - Memory location
# Answer: A formal string for debugging
#
# Explanation:
# __repr__ should return an unambiguous, developer-facing string
# that ideally could be used to recreate the object (e.g. Point(1, 2)).
# __str__ is the "pretty" / user-facing version.
# If __str__ is not defined, print() falls back to __repr__.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # Formal, unambiguous — good for debugging and logs
        return f"Point(x={self.x}, y={self.y})"

    def __str__(self):
        # Informal, human-friendly
        return f"({self.x}, {self.y})"


p = Point(3, 4)
print(f"repr(p) -> {repr(p)}")   # Point(x=3, y=4)  — for debugging
print(f"str(p)  -> {str(p)}")    # (3, 4)           — for users
print(f"p in list -> {[p]}")     # lists use __repr__ on elements
