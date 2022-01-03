# Get the index and the value as a tuple for items in the list
# “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). Result would look like (index, value), (index, value)

l1 = ["hi", 4, 8.99, 'apple', ('t,b', 'n')]
index = 0
l2 = list(enumerate(l1))
print(l2)

tup = [(index, val) for index, val in enumerate(l1)]
print(tup)
