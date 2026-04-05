class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):         # called by str() / print()
        return f"Dog: {self.name}"

    def __len__(self):         # called by len()
        return len(self.name)

d = Dog("Rex")
print(str(d))   # → Dog: Rex
print(len(d))   # → 3