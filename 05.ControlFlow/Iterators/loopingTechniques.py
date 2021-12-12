# to sum up looping techniques:

# 1. enumerate()

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

for i, l1 in enumerate(list1):
    print(l1, list2[i])

print()

# also, 
list1 = ['a', 'b', 'c', 'd']

for key , value in enumerate(list1, start=1):
    print(key, value)

print()
# also

for key, value in enumerate(list1):
    print(value, end = ' ')

print()
# zip()

# two similar kind of containers like list-list
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

for l1, l2 in zip(list1, list2):
    print('%d : %s'%(l1, l2))


print()
# 3. using items()

dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'} 

# using items()
for i, j in dict.items():
    print(i, j)

print()
# 4. Using sorted():
#   a. sorted is used to print the container in a sorted order.
#   b. not an in place sorting. so contaner remains as it is.

list = [2, 5, 3, 9, 1, 3, 5]

for i in sorted(list):
    print(i, end = ' ')

print()
# also you can remove the duplicate by using set()
for i in sorted(set(list)):
    print(i, end = ' ')

print()
# 5. Using reversed()
#   a. it prnts the container values in reversed order
#   b. not an inplace sort

list = [2, 5, 3, 9, 1, 3, 5]

for i in reversed(list):
    print(i, end = ' ')

print()
# also
for i in reversed(range(1, 10, 2)):
    print (i, end = ' ')

# this is how this constructor of range working : 
# range(startVal, endVal, incrementer)
# reversed prints in reversed order


