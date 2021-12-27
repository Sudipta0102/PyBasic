from itertools import product

l = [1, 2]
l1 = [3, 4]

print(list(product(l))) # by default it will repeat once i.e. repeat = 1

print(list(product(l, l1))) # this gives normal cartesian product

print(list(product(l, l1, repeat=2))) # this first computes normal cartesian product
# then on that result applies normal cartesian product with a copy that result list
#  once more. because repeat = 2
# In this case, 
# 1. product(l, l1) -> l2
# 2. product(l2, l2) -> output (so it's repeating 2 times)


print(list(product(l, l1, range(0, 2))))
# here, 
# 1. product(l, l1) -> l2 (is 2D list)
# 2. then apply range function on that. In this case range values are 0 to 1
# 3. add 0 to every sub tuple and add 1 to every sub tuple.

