# Q8: What does globals() return?
# Options:
#   - All variables
#   - Only functions
#   - A dictionary of global scope
#   - Module names
# Answer: A dictionary of global scope
#
# Explanation:
# globals() returns a dict representing the current module's global
# symbol table — every name defined at module (top) level: variables,
# functions, classes, imports, etc. It does NOT include local variables
# from inside a function (that's what locals() is for).
# The returned dict is *live* — mutating it actually changes globals.


MY_CONST = 42
greeting = "hello"


def my_function():
    pass


g = globals()

# Show a few interesting keys that exist at module level
for name in ["MY_CONST", "greeting", "my_function", "__name__"]:
    print(f"globals()['{name}'] = {g.get(name)!r}")

# globals() vs locals() inside a function
def demo_scope():
    local_var = "I'm local"
    print(f"  'local_var' in globals()? {'local_var' in globals()}")
    print(f"  'local_var' in locals()?  {'local_var' in locals()}")
    print(f"  'MY_CONST'  in globals()? {'MY_CONST' in globals()}")


demo_scope()

# globals() is live — this actually creates a new global variable
globals()["injected"] = "created via globals()"
print(f"injected = {injected}")
