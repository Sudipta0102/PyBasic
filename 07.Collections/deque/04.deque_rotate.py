from collections import deque

d = deque([2,3,4,5,6])

# for positive argument it will right rorate
d.rotate(1)
print(d)

# for negative argument it will left rorate
d.rotate(-1)
print(d)


