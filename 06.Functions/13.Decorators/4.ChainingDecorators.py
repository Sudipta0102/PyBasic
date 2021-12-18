# decorator chaining is like using multiple decorators at one time. 
def moreOuterDecor(func):
    def inner(x):
        x = func(x)
        return x/x
    return inner    

def outerDecor(func):
    def inner(x):
        x = func(x)
        return x*x
    return inner

def innerDecor(func):
    def inner(x):
        x = func(x)
        return x * 2
    return inner

@moreOuterDecor
@outerDecor
@innerDecor
def num(x):
    return x

print(num(10))    

# it's like saying outerDecor(innerDecor(10))

# and if you add @moreOuterDecor, then it's like saying 
# moreOuterDecor(outerDecor(innerDecor(10)))