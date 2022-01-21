# problem statement: How to get list of parameters name from a function in Python?

# 1. using inspect.signature()
# 2. using inspect.getfullargspec()

import collections
import inspect

print(inspect.signature(collections.Counter))


# user defined func
def mfunc(a, b, *, c, d):
    print(a, b, c, d)


print(inspect.signature(mfunc))

print(inspect.getfullargspec(mfunc))


