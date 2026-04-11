# Q10: What does 'with' manage in file handling?
# Answer: Closing automatically

import os
import tempfile

# Create a temp file for demo
tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
tmp_path = tmp.name
tmp.close()

# === WITH statement: auto-closes the file ===
print("=== With 'with' — auto close ===")
with open(tmp_path, "w") as f:
    f.write("Hello from with!")
    print(f"  Inside 'with': f.closed = {f.closed}")
print(f"  Outside 'with': f.closed = {f.closed}")

# === WITHOUT 'with': must close manually ===
print("\n=== Without 'with' — manual close ===")
f = open(tmp_path, "r")
content = f.read()
print(f"  Before close: f.closed = {f.closed}")
f.close()
print(f"  After close:  f.closed = {f.closed}")
print(f"  Content: {content}")

# === 'with' closes even on exception ===
print("\n=== 'with' closes even on error ===")
try:
    with open(tmp_path, "r") as f:
        data = f.read()
        raise ValueError("Something went wrong!")
except ValueError as e:
    print(f"  Error caught: {e}")
    print(f"  File still closed: f.closed = {f.closed}")

# Cleanup
os.unlink(tmp_path)

# === How it works under the hood ===
print("\n=== Under the hood: __enter__ and __exit__ ===")
print("with open('file') as f:  -->  f = open('file').__enter__()")
print("   ...code...           -->  runs your code")
print("   (block ends)         -->  f.__exit__() called = file closed")