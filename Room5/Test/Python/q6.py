#How do you create a generator expression?
#(x for x in range(5))

gen = (x for x in range(5))
print(type(gen))  # → <class 'generator'>

for val in gen:
    print(val)
# → 0
# → 1
# → 2
# → 3
# → 4