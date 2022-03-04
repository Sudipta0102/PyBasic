import numpy as np

a = np.array([[1, 3, 5, 7, 9, 11],
              [2, 4, 6, 8, 10, 12]])

# horizontal
print(np.hsplit(a, 3))

# vertical
print(np.vsplit(a, 2))
