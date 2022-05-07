import collections


# 1. using count
def func(test_list, freq):
    res = []
    for num in test_list:
        if test_list.count(num) > freq and res.count(num) == 0:
            res.append(num)
    return res


li = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
print(func(li, 3))

# 2. list comprehension + counter
res = [ele for ele, cnt in collections.Counter(li).items() if cnt > 3]
print(res)
print(collections.Counter(li).keys())
print(collections.Counter(li).items())

