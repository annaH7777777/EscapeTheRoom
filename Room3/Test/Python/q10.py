#What is the default encoding used by open() in Python 3?
#UTF-8

f1 = open("file.txt", "r")
f2 = open("file.txt", "r", encoding="utf-8")

print(f1.encoding)  # → cp1252 (on your Windows machine)
print(f2.encoding)  # → utf-8

# So on YOUR system they are NOT equal!
f1.close()
f2.close()