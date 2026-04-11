# Q7: How are private attributes indicated in Python?
# Answer: __ (double underscore)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self._currency = "USD"      # "protected" by convention (single _)
        self.__balance = balance    # private — name mangling (double __)

    def get_balance(self):
        return self.__balance

acc = BankAccount("Anna", 1000)

# Public — works fine
print("=== Public attribute ===")
print(f"acc.owner = {acc.owner}")

# Single underscore — accessible but convention says "don't touch"
print("\n=== Single underscore (convention only) ===")
print(f"acc._currency = {acc._currency}")

# Double underscore — name mangling blocks direct access
print("\n=== Double underscore (private via name mangling) ===")
try:
    print(acc.__balance)
except AttributeError as e:
    print(f"acc.__balance -> AttributeError: {e}")

# Access through method (intended way)
print(f"acc.get_balance() = {acc.get_balance()}")

# Name mangling: Python renames it to _ClassName__attribute
print(f"\n=== Under the hood: name mangling ===")
print(f"acc._BankAccount__balance = {acc._BankAccount__balance}")

# See all attributes
print(f"\n=== All attributes ===")
print([a for a in dir(acc) if 'balance' in a.lower() or 'currency' in a.lower()])