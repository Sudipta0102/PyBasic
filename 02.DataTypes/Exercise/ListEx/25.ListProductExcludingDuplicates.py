from collections import Counter
from functools import reduce
# 1. using counter
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
prod = 1

list_without_duplicates = Counter(test_list).keys()

print(list_without_duplicates)

for num in list_without_duplicates:
    prod *= num

print(prod)

# 2. naive

test_list = [1, 3, 5, 6, 3, 5, 6, 1]
prod = 1
res = [test_list[0]]
for num in test_list:
    if res.count(num) == 0:
        res.append(num)
        prod *= num

print(prod)

# 3. using reduce

test_list = [1, 3, 5, 6, 3, 5, 6, 1]

# list_without_duplicates = list(set(test_list))
# print(list_without_duplicates)

# one liner
product = reduce(lambda x, y: x * y, set(test_list))

print(product)
