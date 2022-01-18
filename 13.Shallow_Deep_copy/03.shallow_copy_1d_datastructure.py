# here we use 'copy' module.
import copy

list_a = [1, 2, 3]
list_b = copy.copy(list_a)

list_b[0] = 10
print(list_a)
print(list_b)

# here the is result is exactly what we expected, original copy doesn't change, only the copied one.
# 1. because it's a 1d data structure and shallow copies are only one level deep.
