# Q5: Which function checks subclass relationships?
# Answer: issubclass()

class Animal:
    pass

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

class Car:
    pass

# === issubclass() — checks CLASS relationships ===
print("=== issubclass(child, parent) ===")
print(f"  issubclass(Dog, Animal)   = {issubclass(Dog, Animal)}")    # direct subclass
print(f"  issubclass(Puppy, Animal) = {issubclass(Puppy, Animal)}")  # indirect subclass
print(f"  issubclass(Animal, Dog)   = {issubclass(Animal, Dog)}")    # reversed -> False
print(f"  issubclass(Car, Animal)   = {issubclass(Car, Animal)}")    # unrelated -> False
print(f"  issubclass(Dog, Dog)      = {issubclass(Dog, Dog)}")       # class is subclass of itself

# === isinstance() — checks OBJECT's class ===
print("\n=== isinstance(object, class) ===")
dog = Dog()
print(f"  isinstance(dog, Dog)    = {isinstance(dog, Dog)}")
print(f"  isinstance(dog, Animal) = {isinstance(dog, Animal)}")  # True — Dog IS-A Animal
print(f"  isinstance(dog, Car)    = {isinstance(dog, Car)}")

# === Key difference ===
print("\n=== Difference between the two ===")
print(f"  issubclass(Dog, Animal) -> checks if CLASS Dog inherits from Animal")
print(f"  isinstance(dog, Animal) -> checks if OBJECT dog is created from Animal (or subclass)")

# === Multiple classes in tuple (both functions support this) ===
print("\n=== Check against multiple classes ===")
print(f"  issubclass(Dog, (Animal, Car))   = {issubclass(Dog, (Animal, Car))}")
print(f"  isinstance(dog, (Animal, Car))   = {isinstance(dog, (Animal, Car))}")

# === Error if you pass an instance to issubclass ===
print("\n=== issubclass needs CLASSES, not instances ===")
try:
    issubclass(dog, Animal)  # dog is an instance, not a class
except TypeError as e:
    print(f"  Error: {e}")
