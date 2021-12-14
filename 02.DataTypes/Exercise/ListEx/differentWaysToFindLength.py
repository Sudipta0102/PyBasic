import operator


l = [1,2,3,4]
# 1. len()
print(len(l))
#print(operator.length_hint(l))
# 2. length_hint()
from operator import length_hint
print(length_hint(l))
# 3. Naive method
counter = 0
for i in l:
    counter+=1
print(counter)
