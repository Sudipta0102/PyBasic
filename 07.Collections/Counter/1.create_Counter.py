from collections import Counter

# creating Counter is like creating a dictionary with number of occurrence of each element.
s = 'aaaaaccaaabbbbbaabbccccc'
counter1 = Counter(s)
print(counter1)


l = ['1', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '3', '3', '3', '3', '1', '1', '1', '1', '1']
counter2 = Counter(l)
print(counter2)

d = {'red': 10, 'blue': 20}
counter3 = Counter(d)
print(counter3)

t = ('1', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '3', '3', '3', '3', '1', '1', '1', '1', '1')
counter4 = Counter(t)
print(counter4)

# because it's a set, technically a counter can be created out of a set. But as set doesn't hold duplicate
# values. It doesn't really make sense
st = {'1', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '3', '3', '3', '3', '1', '1', '1', '1', '1'}
counter5 = Counter(st)
print(counter5)

# using **kwargs
counter6 = Counter(first='ami', second='amii', third='amiii')
print(counter6)

kwargs = {'red': 10, 'blue': 20}
counter7 = Counter(**kwargs)
print(counter7)

