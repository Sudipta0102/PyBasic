input_list = [1, 2, 2, 5, 8, 4, 4, 8]
res = []


from collections import Counter

items = Counter(input_list)
print(items)

items = Counter(input_list).keys()
print(len(items))
