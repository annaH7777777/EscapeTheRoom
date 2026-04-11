# Q5: Which method is called when an object is printed?
# Answer: str (i.e. __str__)

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        """Called by print() and str() — human-readable"""
        return f"{self.name} the {self.species}"

    def __repr__(self):
        """Called by repr() and in the REPL — developer-readable"""
        return f"Pet(name='{self.name}', species='{self.species}')"

pet = Pet("Buddy", "Dog")

# print() calls __str__
print("=== print() calls __str__ ===")
print(pet)

# str() also calls __str__
print(f"\nstr(pet) = {str(pet)}")

# repr() calls __repr__
print(f"\n=== repr() calls __repr__ ===")
print(f"repr(pet) = {repr(pet)}")

# === What if __str__ is not defined? ===
class Animal:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Animal('{self.name}')"

a = Animal("Cat")
print("\n=== Fallback: no __str__, print() uses __repr__ ===")
print(a)

# === Priority ===
print("\n=== Priority ===")
print("print(obj) -> __str__() -> __repr__() (fallback)")