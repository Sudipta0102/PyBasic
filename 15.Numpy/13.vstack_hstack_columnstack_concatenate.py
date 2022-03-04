import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

# vertical stacking
print('Verical Stacking:\n', np.vstack((a, b)))
print('*'*20)

# horizontal stacking
print('Horizontal Stacking:\n', np.hstack((a, b)))
print('*'*20)

c = [5, 6]

# stacking columns
print('column stacking:\n', np.column_stack((a, c)))
print('*'*20)

# concatenation method.
print('Concatenating to 2nd axis:\n', np.concatenate((a, b), axis=1))
print('*'*20)

print('Concatenating to 1st axis:\n', np.concatenate((a, b), axis=0))
print('*'*20)
