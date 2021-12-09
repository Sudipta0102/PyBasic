# immutable targets are like numbers, strings and tuples.

import operator

x = 5
y = 6
a = 5
b = 6

# normal operator
z = operator.add(x, y)

# in-place operator
p = operator.add(a, b)

print("Normal operator addition:", z)
print("inPlace operator addtion:", p)

print("First arg of normal addition:", x)
print("First arg of in-place addition:", a)

# Here, First arg of in-place addition is not changed here because
# arguments are of immutable type. 
