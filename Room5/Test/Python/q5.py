#What is self in class methods?
#Refers to the instance

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I'm {self.name}"

p1 = Person("Alice")
p2 = Person("Bob")
print(p1.greet())  # → Hi, I'm Alice
print(p2.greet())  # → Hi, I'm Bob