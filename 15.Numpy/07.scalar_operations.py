import numpy as np

a = np.array([1, 2, 3, 4])
print('original array:', a)
print('after Adding 2 to every element:', a+2)
print('after subtracting 3 from every element:', a-3)
print('after multiplying 10 to every element:', a*10)
print('after squaring:', a**2)

# in-place multiplication
a *= 2
print('in place multiplication by 2 :', a)
