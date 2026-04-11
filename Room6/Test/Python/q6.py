# Q6: What does super() do?
# Answer: Access parent class methods

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"  Animal.__init__: name={name}")

    def speak(self):
        return "..."

class Dog(Animal):
    def __init__(self, name, breed):
        # super() calls the PARENT's __init__
        super().__init__(name)
        self.breed = breed
        print(f"  Dog.__init__: breed={breed}")

    def speak(self):
        # super() calls the PARENT's speak
        parent_sound = super().speak()
        return f"Woof! (parent said: '{parent_sound}')"

print("=== super().__init__ — calling parent constructor ===")
dog = Dog("Rex", "Shepherd")
print(f"dog.name = {dog.name}")
print(f"dog.breed = {dog.breed}")

print("\n=== super().method() — calling parent method ===")
print(f"dog.speak() = {dog.speak()}")

# === Multiple inheritance: super() follows MRO ===
class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return f"Hello from B -> {super().greet()}"

class C(A):
    def greet(self):
        return f"Hello from C -> {super().greet()}"

class D(B, C):
    def greet(self):
        return f"Hello from D -> {super().greet()}"

print("\n=== super() follows MRO (Method Resolution Order) ===")
d = D()
print(f"d.greet() = {d.greet()}")
print(f"MRO: {[cls.__name__ for cls in D.__mro__]}")