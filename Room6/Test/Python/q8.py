# Q8: Which function loads a module dynamically?
# Answer: importlib.import_module()

import importlib

# === Dynamic import: module name as a string ===
print("=== importlib.import_module() ===")

# Instead of: import math
math_module = importlib.import_module("math")
print(f"math.sqrt(16) = {math_module.sqrt(16)}")
print(f"math.pi = {math_module.pi}")

# Instead of: import json
json_module = importlib.import_module("json")
data = json_module.dumps({"name": "Anna"})
print(f"json.dumps() = {data}")

# === Practical use: load module based on user input ===
print("\n=== Practical: choose module at runtime ===")
modules_to_try = ["os", "sys", "random"]
for name in modules_to_try:
    mod = importlib.import_module(name)
    print(f"Loaded '{name}' -> {type(mod)}")

# === Import submodule ===
print("\n=== Import submodule ===")
path_module = importlib.import_module("os.path")
print(f"os.path.join('a', 'b') = {path_module.join('a', 'b')}")

# === Why not __import__? ===
print("\n=== __import__ works but NOT recommended ===")
m = __import__("math")
print(f"__import__('math').sqrt(9) = {m.sqrt(9)}")
print("Use importlib.import_module() instead — it's the official API")