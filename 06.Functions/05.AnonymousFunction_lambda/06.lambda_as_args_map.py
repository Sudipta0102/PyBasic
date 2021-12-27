# 1. map(func, seq) seq-> like a list or tuple
# 2. returns the map object and can be converted to any iterable
# 3. what it does is, it takes an iterable and runs a formula of some kind on that and helps
# creating a new iterable.

l1 = [1,2,3,4,5,6,7,8,9]
map_obj = map(lambda x: x*10, l1)
print(list(map_obj))

# same thing you can achieve with list_comprehension
l2 = [x*10 for x in l1]
print(l2)

