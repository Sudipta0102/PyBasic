# 1. chain.from_iterable(): 
# This function is implemented similarly as a chain() but the argument 
# here is a list of lists or any other iterable container.
# 2. It takes only one argument and argument needs to be 2D container.
import itertools

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]
t1 = (1, 2, 3)

l4 = [t1, l2]
t2 = (l1, l2)

print(list(itertools.chain.from_iterable(t1)))