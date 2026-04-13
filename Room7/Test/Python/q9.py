# Q9: What is returned by reversed(range(3))?
# Answer: reversed object (an iterator)

result = reversed(range(3))
print(f"reversed(range(3))       = {result}")
print(f"type                     = {type(result)}")
print(f"list(reversed(range(3))) = {list(reversed(range(3)))}")
