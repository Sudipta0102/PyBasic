# 1. To modify the enclosed varible in the local function, 'nonlocal' key word 
# needs to be used.

def outer():
    e = 4
    def inner():
        l = 6
        # to modify,
        nonlocal e
        print("Enclosed before modifying:", e)
        e +=1
        print("Local:", l)
        print("Enclosed after modifying:", e)   
    inner()

outer()        