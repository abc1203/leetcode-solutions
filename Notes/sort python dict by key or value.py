# sort python dict by key
dict = {3: 10, 2: 9, 1: 15, 15: 2, 10: 32}
sorted_keys = sort(list(dict.keys()))
sorted_dict_by_key = {i:dict[i] for i in sorted_keys}
print(sorted_dict_by_key)

# sort python dict by value
dict = {3: 10, 2: 9, 1: 15, 15: 2, 10: 32}
sorted_dict_by_value = dict(sorted(dict.items(), key = lambda item: item[1]))
print(sorted_dict_by_value)
