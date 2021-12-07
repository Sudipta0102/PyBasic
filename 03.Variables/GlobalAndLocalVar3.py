#global scope
s = "beep you too"

def func():
    #local scope
    s = "beep you"
    print(s)

func()
print(s)