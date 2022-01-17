
def fib_generator(n):
    a, b = 0, 1
    idx = 0
    while idx <= n:
        yield a
        a, b = b, a+b
        idx += 1


for i in fib_generator(10):
    print(i)



