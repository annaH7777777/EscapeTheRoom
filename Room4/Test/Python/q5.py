#What happens if you modify a list while iterating over it?
#Unpredictable behavior

# Delete by index
numbers = [1, 2, 3, 4, 5, 6]
for i, n in enumerate(numbers):
    del numbers[i]  # skips every other element
print(numbers)  # → [2, 4, 6] ❌ not empty!