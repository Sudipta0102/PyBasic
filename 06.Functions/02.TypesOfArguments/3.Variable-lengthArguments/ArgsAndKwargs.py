# use both to call the same function
def myFunc1(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

args = [1, 2, 3]
myFunc1(*args)
kwargs = {'arg1': 1, 'arg2': 2, 'arg3': 3}
myFunc1(**kwargs)

# use both kind arguments in the same function call
"use both kind arguments in the same function call"
def myFunc2(*args, **kwargs):
    print(args)
    print(kwargs)

args = [1, 2, 3]
kwargs = {'arg1': 1, 'arg2': 2, 'arg3': 3}    
myFunc2(args, kwargs)

