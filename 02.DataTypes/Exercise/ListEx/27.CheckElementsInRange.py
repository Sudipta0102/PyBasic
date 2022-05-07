test_list = [4, 5, 6, 7, 3, 9]
i, j = 5, 10

for num in test_list:
    if i > num or num < j:
        print("outta range")
        break
else:
    print("in range")


# 2. using all()
res = all(ele for ele in test_list if i > ele < j)
print(res)


