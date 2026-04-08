#What does yield do in Python?
#Returns a generator

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(3):
    print(num)
# → 1
# → 2
# → 3