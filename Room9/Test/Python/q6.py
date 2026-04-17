# Q6: How do you read only the first line of a text file?
# Options:
#   - file.readlines(1)
#   - file.read(1)
#   - file.readline()
#   - file.firstline()
# Answer: file.readline()
#
# Explanation:
# file.readline()  → reads ONE line (up to and including '\n') and returns
#                    it as a string. Exactly what the question asks for.
# file.read(1)     → reads ONE CHARACTER, not a line.
# file.readlines(1)→ the hint (sizehint=1) is an approximate byte budget
#                    and still returns a LIST of lines, not a single line.
# file.firstline() → not a real method.


import os
import tempfile

# Build a small sample file so the demo is self-contained
path = os.path.join(tempfile.gettempdir(), "q6_sample.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write("first line\nsecond line\nthird line\n")

# Correct answer in action:
with open(path, "r", encoding="utf-8") as f:
    first = f.readline()
print(f"readline()     -> {first!r}")     # 'first line\n'

# Compare with the distractors:
with open(path, "r", encoding="utf-8") as f:
    one_char = f.read(1)
print(f"read(1)        -> {one_char!r}")  # 'f'  — just one character

with open(path, "r", encoding="utf-8") as f:
    hinted = f.readlines(1)
print(f"readlines(1)   -> {hinted!r}")    # ['first line\n'] — still a list

os.remove(path)
