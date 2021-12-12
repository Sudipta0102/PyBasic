# 1. Iterator is an object what we used to iterate over iterable objects like 
# list, tuple, dictionary and sets.
# 2. Iterator object is initialized using iter() method.
# 3. And for iteration, it uses next() method.


# 1. __iter(iterable)__ method that is called  for the initialization of an
# iterator. And return an iterator object. this goes like below:
iterable_value = 'amise'
iterable_object = iter(iterable_value)

while True:
    try:
        # 2. iterate by calling next
        item = next(iterable_object)
        # here you do your work, in this case just printing
        print(item, end = ' ')

    # 3. until Stopiteration
    except StopIteration:
        break

# A simple program where from 10 to given limit need to be printed.

class Test:

    # constructior
    def __init__(self, limit):
        self.limit = limit

    # creates iterator object.
    # called when iterator is initialized.
    def __iter__(self):
        self.x = 10 # because 10 it should print
        return self

    # Now, to move to the next element, in python 3, you need to replace 
    # next with __next__
    def __next__(self):

        #  storing the current value of x which is 10
        x = self.x

        # stop iteration if the limit is reached.
        if x > self.limit:
            raise StopIteration

        # Else increament and return the old value
        self.x = x+1;
        return x;

print()
for i in Test(15):
    print(i, end = ' ')

