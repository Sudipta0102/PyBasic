import numpy as np

arr = np.arange(0, 12)
print(arr)

arr = arr.reshape(3, 4)
print(arr)

for x in np.nditer(arr):
    print(x, end=' ')
print()
print('*'*20)

arr = np.arange(0, 12)
print(arr)

arr = arr.reshape(3, 4)
arr = arr.T
print(arr)

for x in np.nditer(arr):
    print(x, end=' ')
print()
print('*'*20)