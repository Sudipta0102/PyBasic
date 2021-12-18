# also, converting the functionality into a class and implementing 
# the __iter__() method. Because it creates the iterator object every time
# so you don't have to recreate the generator again and again.
# 

class iterable(object):
    def __iter__(self):
        x = 1;
        yield x
        yield x + 1
        yield x + 2

itr = iterable()

for i in itr:
    print(i, end = ' ')

for i in itr:
    print(i*2, end = ' ')

for i in itr:
    print(i*3, end = ' ')    