def func(x, y=10):
    print(x)
    print(y)
    print()


func(11)
func(11, 12)


# here y is default argument. If no value is given when calling the function 
# then 10 would be the default value in this case

# only one rule: all non default argument should be there at the beginning.


def func1(x=1, y=2, z=3):
    print(x)
    print(y)
    print(z)
    print()


# all the arguments can have default values
func1()
# important point : if there are more than 1 default argument and
# you want to change value of any later argument, then mention the
# variable name like below    
func1(y=10) 
func1(z=30)
func1(y=10, z=30)

