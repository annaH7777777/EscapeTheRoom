#Which of these statements creates a set?
#set()

print(type([]))     # → <class 'list'>
print(type({}))     # → <class 'dict'>  ← surprise!
print(type(()))     # → <class 'tuple'>
print(type(set()))  # → <class 'set'>   ✅