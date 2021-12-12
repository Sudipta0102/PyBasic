def iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


mixedList = [34, [4, 5], (4, 5), {"a":4}, "dfsdf", 4.5]

#mixedListIter = iter(mixedList)

for i in mixedList:
    print(iterable(i))

