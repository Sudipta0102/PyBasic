test_list = [5, 6, [], 3, [], [], 9]

res = [ele for ele in test_list if ele != []]
print(res)

res1 = [ele for ele in test_list if ele]
print(res1)

res2 = list(filter(None, test_list))
print(res2)