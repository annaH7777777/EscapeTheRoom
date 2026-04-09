def even_indexed(lst):
    result = []
    
    for i, value in enumerate(lst):
        if i % 2 == 0:
            pair = (value, i)
            result.append(pair)
    
    return result
    
    
if __name__ == "__main__":
    print(even_indexed(['a', 'b', 'c', 'd', 'e']))
