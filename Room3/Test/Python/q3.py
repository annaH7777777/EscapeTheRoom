#What does the yield keyword do?
#Returns a generator object
def count_up(n):
    for i in range(n):
        yield i  # pauses here each time

gen = count_up(3)  # returns a generator object
print(next(gen))   # → 0
print(next(gen))   # → 1
print(next(gen))   # → 2