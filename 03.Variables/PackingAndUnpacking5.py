# In this, i want to mix normal arguments and unpacking concept together
def func(a, **args):
    print(a)
    for key in args:
        print(args[key])

d = {'1':22, '2': 23}
# ** because this is a dictionary
func(12, **d)
