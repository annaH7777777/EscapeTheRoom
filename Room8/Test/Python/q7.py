# Q7: How do you make a class iterable?
# Options:
#   - Add __iter__() method
#   - Add __next__()
#   - Inherit list
#   - Use yield
# Answer: Add __iter__() method
#
# Explanation:
# An object is *iterable* if it defines __iter__(), which must return
# an *iterator*. An *iterator* is what defines __next__() (and also
# __iter__ returning self).
# So:
#   - __iter__  makes a class iterable (usable in a for-loop).
#   - __next__  is what an iterator uses to produce the next value.
# You can combine them in one class, or have __iter__ return a generator
# (which is itself a ready-made iterator — that's where `yield` fits in).
# Inheriting from list would work too, but that's not the standard way
# to make any class iterable.


class Countdown:
    """Iterable class: counts down from `start` to 1."""

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # Returning a generator is the simplest way — it implements __next__ for us.
        n = self.start
        while n > 0:
            yield n
            n -= 1


# Works in a for-loop because of __iter__
for num in Countdown(5):
    print(num, end=" ")
print()

# Also works with other iterable consumers
print(f"list:  {list(Countdown(3))}")
print(f"tuple: {tuple(Countdown(3))}")
print(f"sum:   {sum(Countdown(5))}")   # 5+4+3+2+1 = 15


# Alternative: explicit iterator with __iter__ + __next__
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self        # the object is its own iterator

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current


print(f"Counter(3) -> {list(Counter(3))}")   # [1, 2, 3]
