# Q5: What is duck typing in Python?
# Options:
#   - Type checking based on name
#   - Type checking at runtime
#   - Behavior-based typing
#   - Static typing
# Answer: Behavior-based typing
#
# Explanation:
# "If it walks like a duck and quacks like a duck, it's a duck."
# Python doesn't care about an object's actual class — only whether
# it *behaves* the way the code needs (has the right methods/attributes).
# Runtime type checking happens too, but duck typing specifically means
# judging objects by their behavior/interface, not their declared type.


class Duck:
    def quack(self):
        return "Quack!"

    def walk(self):
        return "Waddling..."


class Person:
    def quack(self):
        return "I'm pretending to be a duck!"

    def walk(self):
        return "Walking on two legs..."


class Car:
    def drive(self):
        return "Vroom!"


def make_it_quack(thing):
    # No type check — we just call .quack().
    # Any object with a quack() method works, regardless of its class.
    return thing.quack()


print(make_it_quack(Duck()))     # Quack!
print(make_it_quack(Person()))   # I'm pretending to be a duck!

# A Car has no quack() -> AttributeError at runtime (duck typing failure)
try:
    make_it_quack(Car())
except AttributeError as e:
    print(f"Car can't quack: {e}")
