# Q6: What does super().__init__() call?
# Answer: Parent constructor

class Vehicle:
    def __init__(self, brand, wheels):
        print(f"  Vehicle.__init__ running: brand={brand}, wheels={wheels}")
        self.brand = brand
        self.wheels = wheels

class Car(Vehicle):
    def __init__(self, brand, model):
        # Call the PARENT's __init__ to set brand and wheels
        super().__init__(brand, wheels=4)
        print(f"  Car.__init__ running: model={model}")
        self.model = model

print("=== Creating a Car (which calls Vehicle.__init__ first) ===")
car = Car("Toyota", "Corolla")
print(f"\nResult: brand={car.brand}, wheels={car.wheels}, model={car.model}")

# === Without super().__init__() — parent attributes never get set ===
print("\n=== What happens WITHOUT super().__init__()? ===")

class BadCar(Vehicle):
    def __init__(self, brand, model):
        # Forgot to call super().__init__() !
        self.model = model

bad = BadCar("Toyota", "Corolla")
print(f"  bad.model = {bad.model}")
try:
    print(f"  bad.brand = {bad.brand}")
except AttributeError as e:
    print(f"  Error accessing brand: {e}")
    print(f"  -> brand was never initialized because parent __init__ didn't run")

# === Why use super() instead of Vehicle.__init__() directly? ===
print("\n=== Why super() vs explicit parent name? ===")
print("  super().__init__()  -> works with multiple inheritance (follows MRO)")
print("  Vehicle.__init__()  -> works but breaks with multiple inheritance")
