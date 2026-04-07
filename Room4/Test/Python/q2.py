#Which keyword is used to create an iterator class?
#class

class CountUp:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):   # makes it iterable
        return self

    def __next__(self):   # defines what comes next
        if self.current >= self.limit:
            raise StopIteration  # signals the end
        self.current += 1
        return self.current

# Using it:
counter = CountUp(3)
for n in counter:
    print(n)
# → 1
# → 2
# → 3