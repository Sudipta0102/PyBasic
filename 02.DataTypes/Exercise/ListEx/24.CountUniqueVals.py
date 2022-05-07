from collections import Counter

input_list = [1, 2, 2, 5, 8, 4, 4, 8]
res = [input_list[0]]
for num in input_list:
    if res.count(num) == 0:
        res.append(num)
print(res)
print(len(res))

# 2. using counter
items = Counter(input_list)
print(items)

items = Counter(input_list).keys()
print(len(items))


