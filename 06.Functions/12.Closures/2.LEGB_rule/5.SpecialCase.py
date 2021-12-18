# if one varible is named same in every scope
# 1. it takes the value in whichever block the operation is being done using the variable.
# 2. follows LEGB rule. it goes like this,
#    a. First it searches the local(L), if it couldn't find the name(x)
#    b. Then it goes to Enclosed(E) level, if it couldn't find the name(x) too
#    c. After that, it goes to the Global(G) level, if unable to find the same
#    d. Then it goes to built-in(B) keyword level, if still it doesn't get that
#    Then, program terminates by giving a NameError.
#

x = 10
def outer():
    x = 9
    def inner():
        x = 8
        print(x)
        
    inner()
    print(x)

outer()        
print(x) 