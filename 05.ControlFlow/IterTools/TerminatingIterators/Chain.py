# chain() takes n number of arguments and returns then one after another
import itertools
from typing import Dict

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]
t1 = (1, 2, 3)
d1 = {1:'a', 2: 'b'}

print(list(itertools.chain(l1, l2, l3, t1, d1)))