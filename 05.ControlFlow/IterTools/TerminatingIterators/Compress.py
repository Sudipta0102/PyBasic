# 1. compress() takes an iterable and a boolean list. 
# 2. boolean list is a mandatory argument here
# 3. depending on the boolean list, the value gets printed if it's true for the
# corresponding index irrecpective of the length of iterable.
import itertools

print(list(itertools.compress('ABC', [0,0,0,0,0,1])))
print(list(itertools.compress('ABC', [1, 1])))