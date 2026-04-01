#Fix this function to return the middle character(s) of a string

def get_middle(s):
    if len(s) % 2 == 0:
        return s[len(s) // 2]
    else:
        return s[len(s)//2 - 1 : len(s)//2 + 1]

print(get_middle("test")) #It should return "es" in this case