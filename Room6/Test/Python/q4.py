# Q4: What is exception chaining used for?
# Answer: Raising a new exception while preserving the old one

# === Explicit chaining with "raise ... from ..." ===
def read_config(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError as original:
        # Raise a new, more meaningful error but KEEP the original cause
        raise RuntimeError(f"Failed to load config: {path}") from original

print("=== Explicit exception chaining (raise ... from ...) ===")
try:
    read_config("missing_file.txt")
except RuntimeError as e:
    print(f"Caught: {e}")
    print(f"Original cause: {e.__cause__}")
    print(f"Cause type: {type(e.__cause__).__name__}")

# === Implicit chaining (happens automatically inside except block) ===
print("\n=== Implicit chaining (automatic inside except) ===")
try:
    try:
        int("not_a_number")
    except ValueError:
        # This new error automatically remembers the ValueError
        raise TypeError("Conversion logic failed")
except TypeError as e:
    print(f"Caught: {e}")
    print(f"Implicit context: {e.__context__}")

# === Summary ===
print("\n=== Key difference ===")
print("raise X from Y  -> e.__cause__   (explicit, intentional)")
print("raise X          -> e.__context__ (implicit, automatic)")