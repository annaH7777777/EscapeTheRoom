def group_by_first(tuples_list):
    result = {}
    
    for key, value in tuples_list:
        if key not in result:
            result[key] = []
        result[key].append(value)
    
    return result

if __name__ == "__main__":
    print(group_by_first([('a', 1), ('b', 2), ('a', 3)]))
