test_list = ["geeks", "for", "geeks", "is", "best"]

s1 = test_list[0][::-1]
# 1. naive
for i in range(len(test_list)):
    test_list[i] = test_list[i][::-1]

print(test_list)


# 2. list comprehension
test_list = ["geeks", "for", "geeks", "is", "best"]

res = [i[::-1] for i in test_list]
print(res)

# 3. map()
test_list = ["geeks", "for", "geeks", "is", "best"]

# reverse = lambda i: i[::-1]
res = list(map(lambda i: i[::-1], test_list))
print(res)

