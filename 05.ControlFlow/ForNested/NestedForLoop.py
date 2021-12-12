# we can have any type of loop inside any type of loop

from __future__ import print_function # i need to know more about this line

for i in range(1, 6):
    for j in range(i):
        print(i, end = ' ')
    print()
