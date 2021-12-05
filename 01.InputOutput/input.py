# input() function is required to take input. It will automatically 
# identifies the type of input
# if not correct input, then either syntax error or exception

val = input("enter your value:") #input 2
print(val) # prints 2
print(type(val))

val = input("enter your value:") # input 2
print(val*2) # prints 22 not 2*2=4
# because val is string here
print(int(val)*2) # this will print 4 because val is converted to int