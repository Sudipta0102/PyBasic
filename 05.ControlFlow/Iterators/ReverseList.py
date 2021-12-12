# built in reverse function
from typing import Counter


lst = [10, 11, 12, 13, 14, 15]
lst.reverse()
print(lst)

fruits = ['apple', 'Lemon', 'Appple']
# using the slicing technique
print(fruits[::-1])

# using for loop
lst = [10, 11, 12, 13, 14, 15]
print([element for element in reversed(lst)])

# using while loop 1
lst = [10, 11, 12, 13, 14, 15]
n = len(lst)-1
while n>=0:
    print(lst[n] , end = ' ')
    n -= 1
print()    

# using while loop 2
lst = [10, 11, 12, 13, 14, 15]
revList = []
while lst:
    revList.append(lst.pop())
print(revList)

