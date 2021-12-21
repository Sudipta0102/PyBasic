# 1. zip() combines similar type of iterators. (List-List, dict-dict)
# 2. it takes the length of lesser size list. other items will be skipped.

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
t = ()
for l1, l2 in zip(list1, list2):
    #print('%d : %s'%(l1, l2))
    t = (t + (l1, l2)) # fact: tuple doesn't have append method, but you can concatenate
print(t)