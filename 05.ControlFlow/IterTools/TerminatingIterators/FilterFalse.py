# filterfalse() takes two arguments, one func and one container. 
# this method iterates through the container and prints value only
# when passed func returns false.
# filterfalse(func, iterable)

import itertools

li = [2, 4, 8, 7, 8]

print(list(itertools.filterfalse(lambda x: x%2==0, li )))