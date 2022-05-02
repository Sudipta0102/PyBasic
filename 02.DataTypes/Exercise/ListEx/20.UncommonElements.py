test_list1 = [[1, 2], [3, 4], [5, 6]]
test_list2 = [[3, 4], [5, 7], [1, 2]]

res_list = []
for i in test_list1:
    if i not in test_list2:
        res_list.append(i)

for i in test_list2:
    if i not in test_list1:
        res_list.append(i)

print(res_list)


list1 = [[1, 2], [3, 4], [5, 6]]
list2 = [[3, 4], [5, 7], [1, 2]]

res_set = set(map(tuple, list1)) ^ set(map(tuple, list2))
res_list = list(map(list, res_set))

print(res_list)
