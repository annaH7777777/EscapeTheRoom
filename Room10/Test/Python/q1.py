# Q1: Which method allows an object to be used in a for loop?
# Options:
#   - __next__()
#   - __iter__()
#   - __call__()
#   - __loop__()
# Answer: __iter__()
#
# Explanation:
# Python's for loop works with any object that implements the *iterator
# protocol*. The protocol has two parts:
#   - __iter__(self) must return an iterator object (often self).
#   - __next__(self) returns the next value, or raises StopIteration.
# The for loop first calls iter(obj), which invokes __iter__, then
# repeatedly calls next() on the result (which invokes __next__).
# So __iter__ is what *makes* an object usable in a for loop — without
# it, Python raises TypeError: '... object is not iterable'.
# __call__ makes an instance callable like a function (obj()).
# __loop__ is not a real dunder method.


class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # Returning self means this class is both iterable AND its own iterator
        self.current = self.start
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


for n in Countdown(3):
    print(f"tick: {n}")        # 3, 2, 1

# Works with any iterable-consuming function too:
print(f"as list -> {list(Countdown(5))}")   # [5, 4, 3, 2, 1]