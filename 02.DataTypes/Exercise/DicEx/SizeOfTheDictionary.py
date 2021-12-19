# The size of a Dictionary means the amount of memory( in bytes) occupied by a Dictionary object.

# with sys.getsizeof(dictionary)

import sys

dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}

print(sys.getsizeof(dic3))

# 2. in built __sizeof__ method

print(dic3.__sizeof__()) # as alaways, this gives the size of the object without additional garbage values.

