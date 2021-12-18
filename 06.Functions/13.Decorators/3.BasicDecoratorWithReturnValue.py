def hello_decorator(func):
    def inner(*args, **kwargs):
        print("Before beginning")
        returned_val = func(*args, **kwargs)
        print("After finishing")
        # here I am returning the value to the original form
        return returned_val
    return inner

@hello_decorator
def addTwoNums(a, b):
    print("in function")
    return a+b

a, b = 1, 2

print(addTwoNums(a, b))