# Q1: How do you pass arguments to a decorator?
# Answer: Wrap decorator inside another function

# --- Example: decorator WITH arguments ---
def repeat(times):
    """Outer function: takes the decorator's arguments"""
    def decorator(func):
        """Middle function: takes the function being decorated"""
        def wrapper(*args, **kwargs):
            """Inner function: takes the decorated function's arguments"""
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

print("=== Decorator WITH arguments (repeat 3 times) ===")
greet("Anna")

# --- Comparison: decorator WITHOUT arguments ---
def simple_decorator(func):
    """Only 2 levels needed when no arguments"""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper

@simple_decorator
def say_bye(name):
    print(f"Bye, {name}!")

print("\n=== Decorator WITHOUT arguments ===")
say_bye("Anna")

# --- Why other options are wrong ---
# *args       -> passes arguments to the wrapped FUNCTION, not to the decorator
# lambda      -> not related to decorator argument passing
# yield       -> used for generators, not decorator arguments