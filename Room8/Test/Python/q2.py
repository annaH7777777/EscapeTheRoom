# Q2: Which magic method initializes an object?
# Options:
#   - __create__
#   - __init__
#   - __build__
#   - __object__
# Answer: __init__
#
# Explanation:
# __init__ is called automatically right after an object is created,
# to set up (initialize) its attributes. It receives 'self' (the new
# instance) plus any arguments passed to the class call.
# Note: __new__ actually *creates* the object, then __init__ initializes it.
# __create__ and __build__ are not real Python magic methods.


class Person:
    def __init__(self, name, age):
        # Initializes the new instance's attributes
        print(f"__init__ called for {name}")
        self.name = name
        self.age = age


# Calling Person(...) triggers __init__ automatically
p = Person("Anna", 25)
print(f"Created: {p.name}, age {p.age}")
