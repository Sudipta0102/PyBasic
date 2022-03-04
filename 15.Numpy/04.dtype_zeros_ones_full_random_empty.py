import numpy as np

# 1. datatype of the elements can be changed using dtype.
# built-in python types: int, bool, float, complex, bytes, str
arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
print(arr)
print('*'*20)

# 2. creating a 3X4 matrix using zeros()
# dimension can be given as a form of tuple.
arr = np.zeros((3, 4))
print(arr)
print('*'*20)
# default datatype of elements is float when vector or matrix created using zeros()
# that can be changed using dtype
arr = np.zeros((3, 4), dtype=int)
print(arr)
print('*'*20)

arr = np.zeros([3, 4], dtype=int)
print(arr)
print('*'*20)

# 3. same can be done with one()
arr = np.ones((3, 4), dtype=int)
print(arr)
print('*'*20)

# 4. for creating constant value array you can use full()
arr = np.full((3, 4), 5, dtype=str)
print(arr)
print('*'*20)

# 5. same kind of array can be created using random numbers.
arr = np.random.randint(1, 11, (3, 4))
print(arr)
arr = np.random.random((3, 4))
print(arr)
print('*'*20)

# 6. Empty arrays
arr = np.empty(2, dtype=int, order='C')
print(arr)
print('*'*20)

arr = np.empty([2, 2], dtype=int)
print(arr)
print('*'*20)

arr = np.empty([3, 3])
print(arr)
print('*'*20)


