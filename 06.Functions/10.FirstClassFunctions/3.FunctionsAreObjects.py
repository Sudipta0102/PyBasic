# function can be treated like objects.
def shout(text):
    return text.upper()

print(shout('hi'))

# here, we are assigning the function to a variable. this assignment
# doesn't call the function. What it does is:
# it takes the function object referenced by 'shout' and creates
# a name variable named 'scream' pointing to that same object reference.  
scream = shout

# these two are same
print(scream)
print(shout)

print(scream('hi'))