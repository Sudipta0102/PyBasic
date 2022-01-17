# let's say, in a situation where you are working with a list. Now,
# the thing with the list is, it takes a tangible memory. So, larger 
# the list, larger the memory spaces. 
#   But if there is a some certain pattern on which the list elements 
# are being put, then instead of that list we can use a generator that
# will produce those values whenever you require them. 
# 
# Example: Lets say, the list contains squares 1 to 10. So now, instead 
# of that list, you can create a generator. like this,

def square(x=0):
    while x<10:
        x = x + 1;
        yield x*x

for i in square():
    print(i, end = " ")
print()
# again, later if you need, do the same thing or different
for i in square():
    print(i+1, end = " ")    
print()
# you can change the starting value too..
for i in square(5):
    print(i, end = " ")    
# my point is, you can yield that list and also can manipulate without 
# using extra memory.
# Memory is being saved here, But i dunno about the time complexity. says 
# it's faster but I doubt it :P

# also you can convert this into a list using list comprehension
print()
finalList = [i for i in square()]
print(finalList)
# or the list() can be used
finalList = list(square())
print(finalList)