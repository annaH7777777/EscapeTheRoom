#Fix the code to return a list of squares of all numbers (integers only) in a list.

def squares(lst):
    result = []
    for num in lst:
        if isinstance(num, int):      #float is always true, so we check it only for int and by using isinstance 
            result.append(num*num)
    return result

print(squares([1, 2, "three", 4, "five"]))
