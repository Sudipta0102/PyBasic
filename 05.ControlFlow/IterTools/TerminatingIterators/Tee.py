# tee() takes an iterator and a count 

from itertools import tee
import itertools

li = [2, 4, 6]
count = 3
# storing that in an iterator
itr = iter(li)

# passing the iterator onto tee()
it = tee(itr, count)

#printing the values
for i in range(0, count):
    print(list(it[i]))


print('\r')
# also, you can do that directly in the for loop
for i in itertools.tee([1, 3, 5], 4):
    print(list(i))

# also, this below:
itr1, itr2 = itertools.tee([0, 1, 2], 2)

print(list(itr1))
print(list(itr1)) # iterator you can not use for more than more than once
                  # that why it gives empty list
print(list(itr2))