# 1. zip_longest(iterable1, iterable2, fillVal)
# 2. result iterable will be tulples filled with alternate values. 
# 3. if one iterable is shorter than the other. then remaining element of the 
# container of longer length will form tuples with the fillvalue. 
# 4. fillValue is optional. if absent, then will be filled by string 'None'

import itertools

x = [1, 2, 3, 4, 5]
y = [1, 2, 3]
z = list(itertools.zip_longest(x, y))
print(z)

z1 = list(itertools.zip_longest(x, y, fillvalue='-')) # you will need to 
                                                      # write 'fillvale= '-''
                                                      # otherwise third parameter
                                                      # will be treated as another 
                                                      # container.
print(z1)



