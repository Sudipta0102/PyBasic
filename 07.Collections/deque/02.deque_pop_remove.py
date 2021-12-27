from collections import deque
# 1.
# deque takes two args.
# 1. iterable
# 2. maxlen
# when appending, if it exceeds maxlen then
#   a. current element will get added accordingly
#   b. but it will also pop from the opposite side to maintain maxlen. That means,
#           ->  if maxlen exceeds during an append(), then it will popleft
#           -> and if maxlen exceeds during an appendleft(), then it will pop()

l = [1, 2, 3]

d = deque(l, 4)
print(d)

d.append(5)
print(d)

d.append(6)
print(d)

d.appendleft(7)
print(d)

# 2. pop()
d.pop()
print(d)

# 3. popleft()
d.popleft()
print(d)

# 4. remove() a particular element
# but if iot doesn't find the element, throws a ValueError (be careful here) 
d.remove(3)
print(d)

d.remove(3)
print(d)

