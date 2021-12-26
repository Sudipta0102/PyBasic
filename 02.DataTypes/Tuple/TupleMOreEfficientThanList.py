import sys
import timeit
# List takes more size than tuple of same length and element

l1 = [1,2,3,4]
t1 = (1,2,3,4)

print(sys.getsizeof(l1)) # 120 bytes
print(sys.getsizeof(t1)) # 72 bytes

# Tuple takes lesser time
print(timeit.timeit(stmt="[1,2,3,4]", number=1000000))
print(timeit.timeit(stmt="(1,2,3,4)", number=1000000))

