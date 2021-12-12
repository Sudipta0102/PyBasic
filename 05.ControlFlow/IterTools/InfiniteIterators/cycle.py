# cycle()  

import itertools
from typing import Iterator

list = [1,2]
count = 0

for i in itertools.cycle('AB'):
    if count>6: #
        break
    else:
        print(i, end = ' ')
        count += 1

print()
# using next()
list = [1, 2]
count = 0

Iterators = itertools.cycle(list)

for i in range(6):
    print(next(Iterators), end = ' ')

