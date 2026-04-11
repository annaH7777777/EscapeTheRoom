# Q3: Which keyword is used to define a static method?
# Answer: @staticmethod

class MathUtils:
    @staticmethod
    def add(a, b):
        """No 'self' or 'cls' — just a plain function inside a class"""
        return a + b

    @classmethod
    def description(cls):
        """For comparison: @classmethod receives 'cls'"""
        return f"I am {cls.__name__}"

    def regular(self):
        """For comparison: regular method receives 'self'"""
        return "I need an instance"

# Static method — works without creating an instance
print("=== @staticmethod ===")
print(f"MathUtils.add(3, 7) = {MathUtils.add(3, 7)}")

# Also works on an instance (but no point)
obj = MathUtils()
print(f"obj.add(3, 7) = {obj.add(3, 7)}")

# Comparison with @classmethod
print("\n=== @classmethod (receives cls) ===")
print(MathUtils.description())

# Comparison with regular method
print("\n=== Regular method (requires self) ===")
print(obj.regular())
try:
    MathUtils.regular()
except TypeError as e:
    print(f"MathUtils.regular() fails: {e}")