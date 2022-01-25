import numpy as np

# Initial Array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

print(arr)
print('*'*20)

# 1. normal printing of a single element
print(arr[0][3])
print('*'*20)
# 2. printing of ELEMENTS of specific indexes
idx_arr = arr[[0, 1, 2],
              [2, 3, 1]]

print(idx_arr)
print('*'*20)
# 3. Printing range of elements using indices.
# a. this is first two rows and every columns.
print(arr[:2, :])
print('*'*20)

# b. this is first two rows and two columns.
print(arr[:2, :2])
print('*'*20)

# c. this is first two rows and alternate columns(i.e 0 and 2 in this case)
print(arr[:2, ::2])
print('*'*20)

# d. only alternate rows (0 and 2) and all columns
print(arr[::2, :])
print('*'*20)

# e. alternate rows starts from 1st row and all columns.
print(arr[1::2, :])
print('*'*20)

# f. row ranges from 1 to 2 and all columns. Notice how 3 is exclusive here consistent with the range function.
print(arr[1:3, :])
print('*'*20)

arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

# 4. boolean way of accessing elements
cond = arr > 0
temp = arr[cond]
# returns a 1d array of elements greater than 0.
print(temp)
print(temp.ndim)

