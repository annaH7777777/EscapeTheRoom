#Write a function that merges two sorted lists into a single sorted list without duplicates.
def merge_sorted(a, b):
    return sorted(set(a) | set(b))
    
if __name__ == "__main__" :
  print(merge_sorted([1, 3, 5] , [1, 2, 3]))