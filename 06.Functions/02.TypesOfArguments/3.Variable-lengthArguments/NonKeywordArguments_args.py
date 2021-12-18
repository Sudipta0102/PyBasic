def func(*args):
    for arg in args:
        print(arg)


func(1,2,3,4,5)
l = [1,2,3]
iter_l = iter(l)

print(l)

print(iter_l.__next__())

# things to Notice: *args (that single asterisk there)

# formal and *args
print()
def myFunc(a, *args):
    print(a)
    
    for arg in args:
        print(arg, end = " ")


myFunc(1, 'kllk', 2, 'jkljklljk')