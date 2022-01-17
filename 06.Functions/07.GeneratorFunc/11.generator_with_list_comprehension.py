# Note that, parentheses are being used instead of brackets.
import sys


mygenerator = (i for i in range(1000000))
mylist = [i for i in range(1000000)]

print(sys.getsizeof(mygenerator))
print(sys.getsizeof(mylist))


# also, to convert a generator to a list.
mylist1 = list(mygenerator)
print(sys.getsizeof(mylist1))



