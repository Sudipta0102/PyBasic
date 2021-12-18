# 1. yield in python can be used as the return statement in a function. 
# When done so, instead of returning the value/values, it returns 
# a generator that can be iterated upon.
#
# 2. What excatly happens when you use yield keyword?
# a. Each time you iterate, python runs the code until it encounters a
# yield keyword inside the function.
# b. Then  it causes the function to hand back a generator object to its caller,
# then it sends the yielded value and pauses the function in that state
# without exiting
# c. when this function is called the next time, the state which it was last 
# paused will be remembered and continued with the execution. This will be 
# continued up until the generator is exhausted.
# 
# 3. Ehat does this remembering the state means?
# this means, any local variable that you might have created in the function 
# before calling yield will be available when you invoke this function again.
# Thing to Note:
# This is not the normal functions behave.
# 
# 4. How is it different from 'return'?
# In return, function would have returned the respective values. And all the
# variables you created when running that function will be cleared off when
# when you return something from that function.
# 
# In yield, It will not be cleared off if the generator is not exhausted. all
# the variables and their memory allocations will be still be intact.
# And this function can be used to generate logic defined in the function 
# again and again. so this function becomes a 'genetor function'.

# here's a simple generator
def simple_gen():
    x = 1
    yield x
    yield x+1
    yield x+2

gen_obj = simple_gen()

print(gen_obj) # it's just an address

#but you can iterate through this object
for i in gen_obj:
    print(i)

