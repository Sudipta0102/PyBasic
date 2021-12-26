from collections import Counter

s = 'aaaaaccaaabbbbbaabbccccc'
counter1 = Counter(s)
print(counter1)

# if you use elements(), it returns an iterable. Then that iterable can be converted to
# any datatype like list, tuple etc.
itr = counter1.elements()
l = list(itr)
print(l)

# in single line you can do this though
print(tuple(counter1.elements()))



