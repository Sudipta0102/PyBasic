# Let's say, one function has four arguments and your calling values are in 
# in the form of a list. Now in python, one doesn't have to explicitly
# call every index of that list to fetch all the calling values. That's
# where unpacking concept comes into picture.

def func(a, b, c, d):
    print(a, b, c, d)

my_list = [1,2,3,4]

func(*my_list)
# now with the help of *, we can 'unpack' this list into argument list.
# However, the list elements and the number of arguments needs to same. 
