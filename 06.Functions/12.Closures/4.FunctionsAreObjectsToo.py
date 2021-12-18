def func():
    x = 4
    print("func", x)

func()
print(func) # prints address of the func object.
print(func.__class__) 
print(type(func)) # belongs to function class.