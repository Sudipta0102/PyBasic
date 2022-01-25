import numpy as np

a = np.array([[1, 2],
              [3, 4]])
b = np.array([[4, 3],
              [2, 1]])

print(a+b)
print(a*b) # Note: this is NOT MATRIX MULTIPLICATION, just element-wise multiplication
print(a.dot(b)) # this is MATRIX MULTIPLICATION


