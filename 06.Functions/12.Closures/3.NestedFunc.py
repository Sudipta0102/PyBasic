# 1. a function that is defined in another function is called nested function.
# 2. Nested functions are able to acces variables of the enclosing scope.
# 3. in python, these non-local variables are accessed only within their scope and
# not outside.

def outer_func(text):
    text1 = text

    def inner_func():
        print(text1)

    inner_func() # inner function can be accessed in outer function but not outside that.

if __name__ == '__main__':
    outer_func("the text") 
    #inner_func() can't be called. Because it's not defined in this scope.      