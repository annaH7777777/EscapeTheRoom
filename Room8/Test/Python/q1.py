# Q1: What does the @classmethod decorator do?
# Options:
#   - Makes the method global
#   - Allows method to access class, not instance
#   - Hides method from subclass
#   - Makes method static
# Answer: Allows method to access class, not instance
#
# Explanation:
# A @classmethod receives the class itself as the first argument (cls)
# instead of the instance (self). It can read/modify class-level state
# and is commonly used for alternative constructors (factory methods).


class Dog:
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_species(cls):
        # 'cls' refers to the class, not an instance
        return cls.species

    @classmethod
    def create_puppy(cls, name):
        # Factory method: alternative constructor using the class
        return cls(f"Puppy {name}")

    def instance_info(self):
        # Regular instance method uses 'self' (the instance)
        return f"{self.name} is a {self.species}"


# Call classmethod on the class directly (no instance needed)
print(f"Species (via class):    {Dog.get_species()}")

# Call classmethod on an instance (still gets the class, not the instance)
rex = Dog("Rex")
print(f"Species (via instance): {rex.get_species()}")

# Factory method creates a new instance
buddy = Dog.create_puppy("Buddy")
print(f"Factory-created:        {buddy.instance_info()}")
