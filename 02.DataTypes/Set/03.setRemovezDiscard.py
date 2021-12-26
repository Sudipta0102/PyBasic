setFirst = {1, 2, 3, 4, 9, 7, 5}
# 1. remove() to remove elements.
print(setFirst)
setFirst.remove(1)
print(setFirst)

# 2. discard() to remove elements.
setSecond = {1, 2, 3, 4, 9, 7, 5}
setSecond.discard(10)
print(setSecond)

# the main difference between remove() and discard() is when they attempt to remove or discard an element
# which is not present in the set then,
# 1. remove() gives a keyerror.
# 2. discard() does nothing.
