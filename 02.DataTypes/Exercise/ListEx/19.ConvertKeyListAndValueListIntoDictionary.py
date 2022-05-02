test_list = ["Gfg", 3, "is", 8]
key_list = ["name", "id"]

test_list1 = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
key_list1 = ["name", "number"]

print(len(key_list))
res = []

for idx in range(0, len(test_list), len(key_list)):
    res.append({key_list[0]: test_list[idx], key_list[1]: test_list[idx+1]})

print(res)
