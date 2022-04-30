def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def swapAnother(val1, val2):
    val1, val2 = val2, val1


l = [1,2,3,4,5,6,7,8]
print(swap(l, 2, 5))

l1 = [1,2,3,4,5,6,7,8]
swapAnother(l1[0], l1[2]) # it didn't swap. Why?
# Maybe the value gets swapped, but the object reference l1's first element is different
# than the explicit value I am swapping with. That's why the change doesn't take place
# for the second function.
print(l1)




