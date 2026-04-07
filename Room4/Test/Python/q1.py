#What is a list comprehension?
#A short way to create lists

# Normal loop
squares = []
for x in range(5):
    squares.append(x ** 2)
print(squares)
# → [0, 1, 4, 9, 16]

# List comprehension
squares = [x ** 2 for x in range(5)]
print(squares)
# → [0, 1, 4, 9, 16]