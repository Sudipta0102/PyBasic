nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)

*beginning, last = nums
# notice how beginning is a list even though nums is a tuple.
print(beginning)
print(last)

print('*'*30)

first, *end = nums
print(first)
print(end)

print('*'*30)

first, *middle, last = nums
print(first)
print(middle)
print(last)
