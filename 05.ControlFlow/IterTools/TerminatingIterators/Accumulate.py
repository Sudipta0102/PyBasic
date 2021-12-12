# accmulate(iterable, func)
# 1. func determines what operations to do on iterable
# 2. func is an optional argument. If not given it will do addtion
# 3. if iterable is empty then result also will be an empty iterable.

import itertools

l = [1, 4, 5, 7]

print(list(itertools.accumulate(l))) # here addition takes place
# because no func was mentioned

import operator

print(list(itertools.accumulate(l, operator.mul)))

# question: User defined func can be passed? 


