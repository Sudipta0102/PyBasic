import itertools
import operator

# dropwhile(func, iterable)
# this iterator starts printing values only after the function in argument 
# return false for the first time.

li = [2, 4, 8, 7, 8]

print(list(itertools.dropwhile(lambda x : x%2==0, li)))
