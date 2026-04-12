def intersection(a, b):
    result = []
    for item in a:
        if item in b and item not in result:
            result.append(item)
    return result

if __name__ == "__main__":
    print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))
