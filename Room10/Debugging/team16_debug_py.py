#Fix the code to return "Well done" if their total is above 10.

def check_positive_sum(nums):
    total = 0
    for n in nums:
        if n > 0:
            total += n   # += instead of =+ 
    if total > 10:
        return "Well done"
    return "Try again"

print(check_positive_sum([5, 7]))
