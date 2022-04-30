
list1 = [3, 2, 4]
# 1. traversal
product = 1
for ele in list1:
    product *= ele
print(product)

# 2. numpy.prod
import numpy

print(numpy.prod(list1))

# 3. math.prod
import math

print(math.prod(list1))

# 4. reduce
from functools import reduce
res = reduce(lambda x, y: x*y, list1)
print(res)
