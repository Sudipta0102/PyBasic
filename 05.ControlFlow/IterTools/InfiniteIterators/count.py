# count(start, step) ->step is like the incrementer. Optional argument.
# if not mentioned then by default increments by 1.
# thing to remember : it's an infinite loop. So user needs to 
# break most of the time. 
# Till now, i don't really know where this infinite stream 
# of object has to flow so that we don't have to break. 


# like this
import itertools

for i in itertools.count(5, 10):
    if (i>100):
        break
    else:
        print(i, end = ' ')

