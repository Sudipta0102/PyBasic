test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]

# 1. sort
for ele in test_list:
    ele.sort(reverse=True)

print(test_list)

test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]

# 2. sorted + list comprehension
res = [sorted(ele, reverse=True) for ele in test_list]
print(res)