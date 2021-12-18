# i kinda understand this. but not enough to articulate
# 1. This can be used to change function behaviour
# 2. the outer function always will take the function to be used as an argument.
# which may or may not get manipulated 


# defining a decorator
def hello_decorator(func):
    def inner():
        print("I am before function execution")
        func()
        print("I am after function execution")
    return inner


def func1():
    print("I am function")        

func1 = hello_decorator(func1) # this is equivalent to the @hello_decorator at the top
                               # of func1()

func1()