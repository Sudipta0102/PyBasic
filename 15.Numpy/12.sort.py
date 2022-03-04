import numpy as np

# 1. axis

a = np.array([[1, 4, 2],
              [3, 4, 6],
              [0, -1, -5]])

# sorting row-wise
print(np.sort(a))
print('*'*20)

# sorts all the values and returns a 1-d ndarray
print(np.sort(a, axis=None))
print('*'*20)

# sorting row-wise
print(np.sort(a, axis=1))
print('*'*20)

# sorting column-wise
print(np.sort(a, axis=0))
print('*'*20)

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# 2. kind

# can specify sort algo (OMG!!)
# kind : {'quicksort', 'mergesort', 'heapsort', 'stable'}
# default is quicksort
print(np.sort(a, axis=1, kind='mergesort'))
print('*'*20)

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# 3. order

# setting alias names for dtypes
# info abot S10: 10 here is the maximum length it seems. s is for string.
element_dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]
# values to be put in the array
element_list = [('tumi', 1900, 1.0), ('se', 1895, -3.4), ('ami', 1900, -1.0)]
arr = np.array(element_list, dtype=element_dtypes)
print(np.sort(arr, order='cgpa'))



