from collections import deque

# basically you are extending a queue from both side with an iterable.

d = deque([1,2,3])
print(d)

d.extend([4,4,4])
print(d)

d.extendleft([0,0,0])
print(d)

