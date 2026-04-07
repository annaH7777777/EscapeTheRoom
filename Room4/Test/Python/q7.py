#What does s.strip() do?
#Removes whitespace

s = "  hello  "
print(s.strip())   # → "hello"
print(s.lstrip())  # → "hello  "  (left only)
print(s.rstrip())  # → "  hello"  (right only)