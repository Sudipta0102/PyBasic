# 1. you can import sys. under that getsizeof() function to determine size
#       a. getsizeof() gives size in bytes. 
#       b. the byte size denotes how much memory this tuple object occupied.
#       c. Important Note: sys.getsizeof() returns you marginal space usage,
#       which includes the garbage collection overhead of the object. 
#       so,
# the total space = space occupied by he object + the garbage collection overhead for spaces being occupied.
import sys

t = (1,2,3,4)
t1 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))

print(sys.getsizeof(t))
print(sys.getsizeof(t1))


# does it work on list?
l = [1,2,3,4]
print(sys.getsizeof(l)) # yes, it does.

# 2. the other way is in-built magicmethod __sizeof__()
#       a. Important thing to note here that it gives the value without garbage
#        value overhead space.

t = (1,2,3,4)
t1 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))

print(str(t.__sizeof__()))
print(str(t1.__sizeof__()))

# does it work on list?
l = [1,2,3,4]
print(str(l.__sizeof__())) # yes it does.
