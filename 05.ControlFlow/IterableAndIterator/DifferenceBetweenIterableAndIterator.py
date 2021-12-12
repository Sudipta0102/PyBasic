# 1. iterable is an object, which one can iterate over.
# it generates an iterator when passed to iter() method.

# 2. And Iterator is also an object which is used to iterate over 
# any object using __next__() method, which return the next item of the object

# 3. Every iterator is an iterable but vice verssa is not always true.
# For example a list is an iterable but not an iterator.
# 
#  When a loop is executed,
# 1. a call to iter() on the object is placed.
# 2. If the call is syccessful, this iter() call will return
# an iterator object that defines the method __next__() 
# 3. the __next__() accesses one element at a time from the object.
# 4. StopIteration is raised by __next__() whenever there are no
# more elements to access and thereby results loop termination.


# list of cities
cities = ["Berlin", "Vienna", "Zurich"]

iter_cities = iter(cities)

while True:
    try: 
        print(next(iter_cities))
    except StopIteration:
        print('Done')
        break

