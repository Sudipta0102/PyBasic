from collections import deque

# it's basically a double ended queue
# so you can append and pop from both sides

d = deque()

d.append(1)
d.append(2)
d.appendleft(0)

print(d[0])
