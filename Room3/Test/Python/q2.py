#What does @staticmethod do in Python?
#DAllows the method to be called without creating an instance
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# No instance needed!
result = MathUtils.add(3, 5)  # → 8
print(result)