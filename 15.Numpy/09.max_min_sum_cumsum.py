import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print('largest element is: ', a.max())
print('row-wise largest elements: ', a.max(axis=1))
print('column-wise smallest elements: ', a.max(axis=0))

print('smallest element is: ', a.min())
print('row-wise smallest element is: ', a.min(axis=1))
print('column-wise minimum element: ', a.min(axis=0))

print('sum:', a.sum())
print('cumulative sum of each row:\n', a.cumsum(axis=1))

