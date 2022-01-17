# if you want to have keyword-only arguments, you can do that with asterisk(*). Like below:

def func(a, b, *, c, d):
    print(a, b, c, d)


# now you need to call this function like this:
func(1, 2, c=3, d=4)
# so, after *, every parameter is keyword enforced.


# or, you can do achieve this like below:
def func1(*args, lastbutone, last):
    for arg in args:
        print(arg)
    print(lastbutone)
    print(last)


# this will give errors because 4 and 5 are keyword-only args.
# func1([1, 2, 3], 4, 5)
func1([1, 2, 3], lastbutone=4, last=5)
