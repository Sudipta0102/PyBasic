def func():
    s = 0
    for i in range(10):
        s += i
        yield s


for j in func():
    print(j)
