# Global: Ouside the function
# Enclosing: in the outer() func
# Local: in the inner() func 

g = 10
def outer():
    e = 4
    def inner():
        l = 3
        # this three gives no error
        print("\nFrom local scope")
        print("Local:", l)
        print("global:", g)
        print("enclosing:", e)
    inner()
    print("\nFrom Enclosing scope")
    #print("Local:", l) # this will give error.
    print("global:", g)
    print("enclosing:", e)
    

outer()    
print("\nFrom Global scope")
#print("Local:", l) # this will give error
print("global:", g)
#print("enclosing:", e) # this will give error