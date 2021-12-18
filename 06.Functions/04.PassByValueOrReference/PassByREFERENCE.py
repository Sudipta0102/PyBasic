# 1. Most important thing to note here is, Every variable name is a reference.
# 2. When we pass a variable to a function, a new reference to the object 
# is created.
# 3. Parameter passing in python is reference passing in java.

def myFunc(x):
    x[0] = 20

lst = [1,2,4]
myFunc(lst)
print(lst)
# as you can see above that value gets changed in 0th index. because 
# x is the new reference to the same list.


def myFunc(x):
    x[0] = 20
    return x

# here the above link between passed and received parameter gets broken.
# but why?
# it says, When we pass a reference and change the received reference to 
# something else, then it gets broken
lst=[1,2,4]
print(myFunc(lst))


def myFunc1(x):
    x = [1,2,3]

lst = [4,5,6]
myFunc1(lst)
print(lst)    


# another one where link's broken
def func(x):
    x = 10

x = 20
func(x)
print(x)    

# another one
def swap(x, y):
    temp = x
    x = y
    y = temp

x = 2 
y = 3
swap(x, y)
print(x)
print(y)