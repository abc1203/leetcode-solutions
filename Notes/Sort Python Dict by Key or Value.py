# sort python dict by key
old_dict = {3: 10, 2: 9, 1: 15, 15: 2, 10: 32}
sorted_keys = sort(list(old_dict.keys()))
sorted_dict_by_key = {i:old_dict[i] for i in sorted_keys}
print(sorted_dict_by_key)

# sort python dict by value
old_dict = {3: 10, 2: 9, 1: 15, 15: 2, 10: 32}
sorted_dict_by_value = dict(sorted(old_dict.items(), key = lambda item: item[1]))
print(sorted_dict_by_value)
