# 1. first sorting then loop

def max_and_min(tuple1, k):
    print(tuple1)

    res = [] # ressult will be list consisting of values maximum 2 and minimum 2 values.

    sorted_list = sorted(tuple1)
    print(sorted_list)

    for idx, val in enumerate(sorted_list):
        if idx<k or idx>=len(sorted_list)-k:
            res.append(val)

    res = tuple(res)

    return res        


t = (4,2,7,1,8,7,5,9,2,3)

print(max_and_min(t, 2))

# the same thing can be done by using sorting and slicing.
def max_and_min1(tuple1, k):
    #res = []
    sorted_list = sorted(tuple1)
    res = tuple(sorted_list[:k]+sorted_list[-k:])
    return res

t = (4,2,7,1,8,7,5,9,2,3)

print(max_and_min1(t, 2))
    



