#Which keyword is used to inherit a class?
#class Child(Parent)

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog()
print(dog.speak())
# → Woof!