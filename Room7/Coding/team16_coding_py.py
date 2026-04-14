def lists_to_dict(list1, list2):
    result = {}

    for i in range(min(len(list1), len(list2))):
        result[list1[i]] = list2[i]

    return result

if __name__ == "__main__":
    print(lists_to_dict(['a', 'b', 'c'], [1, 2, 3]))
