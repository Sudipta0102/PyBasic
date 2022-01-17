# way 1: Iterate by calling the function that created the generator 
# in the first place.

# let's do that simple generator again.
def simple_gen():
    x = 1;
    yield x
    yield x + 1
    yield x + 2

# instead of creating the object, iterate through the function itself
for i in simple_gen():
    print(i, end = ' ')

# Now, you can do this as many times as you want
for i in simple_gen():
    print(i, end = ' ')

for i in simple_gen():
    print(i, end = ' ')

for i in simple_gen():
    print(i*2, end = ' ')




