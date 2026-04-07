#What is a decorator in Python?
#A function modifying another function

def my_decorator(func):      # takes a function
    def wrapper():
        print("Before!")
        func()               # calls original function
        print("After!")
    return wrapper           # returns modified function

@my_decorator                # applies the decorator
def say_hello():
    print("Hello!")

say_hello()
# → Before!
# → Hello!
# → After!