#so, to wrap it up for now

a = 1

def func1():
    print("inside func1: ", a)

def func2():
    a = 2
    print("inside func2: ", a)

def func3():
    global a
    a = 3
    print("inside func3: ", a)

print("gobal: ", a)
func1()
print("gobal: ", a)
func2()
print("gobal: ", a)
func3()
print("gobal: ", a)        