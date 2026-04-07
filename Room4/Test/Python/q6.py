#Which method creates an empty dictionary?
#dict()

# Both create empty dictionaries
d1 = dict()  # using the built-in method
d2 = {}      # using literal syntax

print(type(d1))  # → <class 'dict'>
print(type(d2))  # → <class 'dict'>
print(d1 == d2)  # → True