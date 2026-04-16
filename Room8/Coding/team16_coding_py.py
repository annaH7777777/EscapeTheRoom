def merge_dicts(dict_list):
    result = {}
    for d in dict_list:
        result.update(d)
    return result

print(merge_dicts([{"a": 1}, {"b": 2}]))
