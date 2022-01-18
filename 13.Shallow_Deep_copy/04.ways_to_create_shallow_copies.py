import copy

list_a = [1, 2, 3]
# 1. copy.copy()
list_b = copy.copy(list_a)

# 2. using list()
list_c = list(list_a)

# 3. using slicing technique
list_d = list_a[:]

# 4. list.copy()
list_e = list_a.copy()

