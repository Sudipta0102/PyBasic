
a = range(1, 100)

print(a)
print(type(a))
# 1. it returns range object (one kind of iterable)

# size
import sys
print(sys.getsizeof(a)) # prints 48, i dunno what to make of this

# Operations: I think it's essentially a list. So
# any operations that can be done on list can also 
# be done on range() like slicing 
print(a[0:99]) 