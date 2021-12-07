#changing a global variables value in the local scope
s = "beep you"
print(s)
def func():
    #if we just do the below line, then compiler says s is not defined
    #s+="too" 
    #here comes the 'global' keyword
    global s
    s+="too"
    print(s)
    s = "thank you"
    print(s)

func()
print(s)#value here is changed to the last assigned value inside 
#the function...even though we are printing globally!!!
# I think it happens because of the global keyword    