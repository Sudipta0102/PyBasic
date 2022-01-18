import copy

# 2d list
list_a = [[1, 2, 3], [4, 5, 6]]
list_b = copy.copy(list_a)

list_b[0][0] = 10

print(list_a)
print(list_b)

# as it's a 2d list(which is more than 1d data structure) and copy.copy() provides a shallow copy,
# so, it's changing the original list.

