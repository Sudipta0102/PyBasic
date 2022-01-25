import numpy as np

# create a sequence of ints from 0 to 30 with step 5
f = np.arange(0, 31, 5)
print(f)
print('*'*20)

# # Create a sequence of 10 values in range 0 to 5
f = np.linspace(0, 5, 9, dtype=int)
print(f)
print('*'*20)

# reshape() -> can change the dimension of the array.
# but there is a rule.
# let's say, a vector of 8 elements->
# this can be reshaped into (2, 4) or (4, 2), (2, 2, 2)
# because: a1 x a2 x a3 … x aN = b1 x b2 x b3 … x bM (the size should be unchanged)
# in the same way, 3X4 matrix can be reshaped into 2X2X3 or 2X6 matrix
arr = np.full((3, 4), 9, dtype=int)
print(arr)
print('*'*20)

arr = arr.reshape((2, 2, 3))
print(arr)
print('*'*20)


# any matrix can be turned into a vector by flatten()
arr = np.array([[1, 2, 3, 4],
                [5, 2, 4, 2],
                [1, 2, 0, 1]])

print(arr)
print(arr.flatten())
print('*'*20)

