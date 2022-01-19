import numpy as np


A = [[1, 2], [3, 4]]
B = [[4, 5], [6, 7]]
c = [[], []]

for i in A:
    for j in i:
       print(j)


# using numpy
print(np.add(A, B))
print(np.subtract(A, B))

print('*'*30)
# figure out other ways of do9ing it.

X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

result = [[0,0,0],
        [0,0,0],
        [0,0,0]]

# for i in range(len(X)):
#     for j in range(len(X[0])):
#         print(i, j, ":", X[i][j])
#
# print('*'*30)
#
# for i in range(len(Y)):
#     for j in range(len(Y[0])):
#         print(i, j, ":", Y[i][j])


for i in range(len(X)):
    for j in range(len(Y[0])):
        result[i][j] = X[i][j] + Y[i][j]


print(result)


# this doesn't work (obviously)
result1 = [[],[],[]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        result1.append(X[i][j]+Y[i][j])

print(result1)

# list comprehension
result = [[X[i][j]+Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
print(result)


# zip -> this I don't really understand
result = [map(sum, zip(*t)) for t in zip(X, Y)]

for i in result:
    map(print, i) # no output, because it returns a generator


# Explanation :- (I DON'T UNDERSTAND THIS)
# The zip function accepts iterator i of each element(list) of matrix,
# mapping them, adding them using sum() and storing them in the map form.

