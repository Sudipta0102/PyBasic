# Standard Operator: _add_ method takes two arguments, adds variables and
# assigns it to a new variable.
# 
# inplace Operator: on the other hand, _iadd_ method also does the same thing.
# but assigns the result at the 1st argument passed in _iadd_ method.
#
# Now there is a catch.
# catch: There are mutable target like Dictionary, List etc.and then 
# there are immutable targets like number, Strings, tuples etc.
# 1. inplace operator doesn't work effectively on immutable targets. It works 
# like normal operator. Only assignment takes place, no modification of 
# passed argument happens here.
# 2. but inplace operator on iadd works exactly as intended. Here modification
# first argument takes place. 

import operator

a = operator.iadd(1,2)

print(a)

