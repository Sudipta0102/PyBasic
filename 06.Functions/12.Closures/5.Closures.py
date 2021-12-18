# 1. Closure: Function object that remembers values in the enclosing scope 
# even if they are not present in memory.
# 2. Closure needs three things:
#   a. Nested Function
#   b. Nested Function must refer values in the enclosing scope.
#   c. Enclosing function must return nested function.
# 3. Closure has these advantages.
#   a. can avoid global values
#   b. data hiding.



# first nested functions once again.
def outer():
    x = 4
    def inner():
        y = 3
        print(x+y)
    inner()

outer()

# same nested funtions with closure
def outer():
    x = 4
    def inner():
        y = 3
        return  x+y 
    return inner   # here instead of calling the inner function, I returned 
                   # the inner function from outer function. (I can do that because
                   # it's freaking python, you can return functions here.)
                     

a = outer()
print(a) # this a variable is holding the address of inner function
         # because you know, we are returning the inner() from outer()
#print(a.__name__) # says inner if you return inner object instead of inner()   

print(a())

