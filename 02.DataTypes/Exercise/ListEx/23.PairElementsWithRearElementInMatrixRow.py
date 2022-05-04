test_list = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]

res = []

for sub in test_list:
    res.append([[ele, sub[-1]]for ele in sub[:-1]])

print(res)

