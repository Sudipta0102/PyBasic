# this is imlplicit conversion
x = 10
y = 10.5
print("type of x before sum: ", type(x))
print("type of y before sum: ", type(y))
z = x+y
print("sum of x and y:", z)
print("type of z:", type(z))
print("type of x after sum: ", type(x))
print("type of y after sum: ", type(y))
# type of x remains same but when doing the sum it changes 
# the type of x to float 
