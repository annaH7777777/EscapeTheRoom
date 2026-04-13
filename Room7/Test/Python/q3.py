# Q3: What is the result of {i: i*i for i in range(3)}?
# Answer: {0:0, 1:1, 2:4}

# Dict comprehension: {key: value for item in iterable}
result = {i: i*i for i in range(3)}
print(f"{{i: i*i for i in range(3)}} = {result}")

# Step-by-step breakdown
print("\n=== Step by step ===")
for i in range(3):
    print(f"  i={i}  ->  key={i}, value={i*i}")

# === Comparison of comprehensions ===
print("\n=== Different comprehensions ===")
list_comp = [i*i for i in range(3)]       # list
set_comp = {i*i for i in range(3)}         # set (no key:value)
dict_comp = {i: i*i for i in range(3)}     # dict (has key:value)
gen_exp = tuple(i*i for i in range(3))     # tuple from generator

print(f"  List:  [i*i for i in range(3)]       = {list_comp}")
print(f"  Set:   {{i*i for i in range(3)}}       = {set_comp}")
print(f"  Dict:  {{i: i*i for i in range(3)}}    = {dict_comp}")
print(f"  Tuple: tuple(i*i for i in range(3))   = {gen_exp}")

# === Key identifier: the colon : ===
print("\n=== How to tell them apart ===")
print("  {} with   key:value  -> dict comprehension")
print("  {} without key:value -> set comprehension")
print("  []                   -> list comprehension")
print("  ()                   -> generator expression")
