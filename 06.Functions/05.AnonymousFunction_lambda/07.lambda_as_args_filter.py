l = [1,2,3,4,5,6,7,8]

filter_obj = filter(lambda x: x%2 == 0, l)
print(list(filter_obj))

# 1. filter(func, seq)
# 2. here filer is almost same as map, other than the fact where a filter will be applied to given sequence
# in this case, from a given sequence we are only fetching the values which is even.

# again, just like map, same you can achieve with list comprehension
ll = [x%2 == 0 for x in l]
print(ll)
# above gives boolean list

# rather,I need to do this,
l2 = [x for x in l if x % 2 == 0]
print(l2)