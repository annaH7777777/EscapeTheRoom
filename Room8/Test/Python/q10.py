# Q10: What does `del obj` do?
# Options:
#   - Deletes obj immediately
#   - Removes reference to obj
#   - Clears contents of obj
#   - Sets obj to 0
# Answer: Removes reference to obj
#
# Explanation:
# `del` does NOT directly destroy an object. It removes the *name*
# (binding/reference) from the current namespace. The object itself
# is only destroyed (garbage-collected) when its reference count
# drops to zero — i.e. when no other name points to it.
# It also does not clear the object's contents or set it to 0.


class Tracker:
    def __del__(self):
        # Called when the object is actually garbage-collected
        print(f"  Tracker {id(self)} is being destroyed")


# Case 1: single reference — `del` drops ref count to 0, object dies
print("Case 1: only one reference")
a = Tracker()
print("  about to 'del a'")
del a
print("  after del a")
# After `del a`, the name 'a' is gone. Trying to use it is an error:
try:
    print(a)
except NameError as e:
    print(f"  NameError: {e}")

# Case 2: multiple references — `del` on one does NOT destroy the object
print("\nCase 2: two references to same object")
x = Tracker()
y = x               # x and y point to the same object
print("  about to 'del x'")
del x               # object is still alive — y still references it
print("  after del x (object still alive because y holds it)")
del y               # now refcount hits 0 -> object destroyed
print("  after del y")

# `del` also works on list items, dict keys, attributes
lst = [10, 20, 30]
del lst[1]
print(f"After del lst[1]: {lst}")        # [10, 30]

d = {"a": 1, "b": 2}
del d["a"]
print(f"After del d['a']: {d}")          # {'b': 2}
