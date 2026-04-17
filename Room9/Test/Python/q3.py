# Q3: How do you define a private method in Python?
# Options:
#   - def __myfunc()
#   - def _myfunc()
#   - def private()
#   - def -myfunc()
# Answer: def _myfunc()
#
# Explanation:
# Python has no true "private" keyword. Instead, there are conventions:
#   - Single underscore prefix (_myfunc): "internal use only" — a hint to
#     other developers that the method is not part of the public API.
#   - Double underscore prefix (__myfunc): triggers *name mangling* —
#     the name becomes _ClassName__myfunc to avoid clashes in subclasses.
#     This is about avoiding collisions, not privacy.
# The idiomatic way to mark a method as private (by convention) is a
# single leading underscore.
# 'def private()' just names a method 'private' — no special meaning.
# 'def -myfunc()' is a syntax error (hyphens aren't allowed in names).


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        # Public API — uses the private helper internally
        self._log(f"deposit {amount}")
        self.balance += amount

    def _log(self, message):
        # Convention: underscore prefix = "treat as private"
        print(f"[internal] {message}")


acc = BankAccount(100)
acc.deposit(50)                       # calls public method
print(f"balance: {acc.balance}")      # 150

# Python does not prevent access — the underscore is only a convention:
acc._log("manual call still works")
