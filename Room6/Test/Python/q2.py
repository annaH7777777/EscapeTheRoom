# Q2: What is a property in Python?
# Answer: A function accessed like an attribute

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Getter — accessed like an attribute, but it's a function"""
        print("  (getter called)")
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter — validates before setting"""
        if value < 0:
            raise ValueError("Radius cannot be negative!")
        print("  (setter called)")
        self._radius = value

    @property
    def area(self):
        """Computed property — calculated on the fly"""
        return 3.14159 * self._radius ** 2

c = Circle(5)

# Accessing like an attribute (no parentheses!) but it runs the function
print("=== Property getter ===")
print(f"Radius: {c.radius}")

print("\n=== Property setter with validation ===")
c.radius = 10
print(f"New radius: {c.radius}")

print("\n=== Computed property ===")
print(f"Area: {c.area}")

print("\n=== Setter rejects negative value ===")
try:
    c.radius = -3
except ValueError as e:
    print(f"Error: {e}")