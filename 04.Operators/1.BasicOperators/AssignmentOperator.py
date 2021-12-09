a = 10

b = a
print(b)

b+=a
print(b)

b-=a
print(b)

b*=a
print(b)
print(type(b))

b/=a
print(b)
print(type(b)) # this is also like implicit conversion

#floor division 
b//=a
print(b)

b*=a
print(type(b))

# to convert it to int again
b = int(b)
print(type(b))

# this is to print the exponential counts
b**=a
print(b)

