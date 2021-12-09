import operator

a = [1, 2, 3, 4, 5]

# normal add method and first argument printing
z = operator.add(a, [1, 2, 3])
print("result: ", z)
print("First Argument: ", a)

y = operator.iadd(a, [1, 2, 3])
print("result: ", y)
print("First Argument: ", a) # the main list is changed now because of inPlace add.
