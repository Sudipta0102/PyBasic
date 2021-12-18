# 1. Partial functions allow us to fix a certain numbers of arguments of a function
# and generate a new function
# 2. Partial functions can be used to derive specialized functions from general 
# functions and therefore help us to reuse our code.

from functools import partial

# here's a normal function
def func(a, b, c, x):
    return 1000*a + 100*b + 10*c + x

# a partial function is called with f and set a as 3, b as 2, c as 1
newFunc = partial(func, a=3, b=2, c=1) 

# calling newFunc()
print(newFunc(x=0))

