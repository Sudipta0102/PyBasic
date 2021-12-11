# a+=b is not always a=a+b

# 1st example
list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 += [2, 3, 4]

print(list1)
print(list2)
# thay are both same. because we are using a+=b operator here,
# compiler making an in place addtion and since, list1 and list2
# are sharing same refernce variable, that's why, they are both same.


# Example 2
list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 = list1 + [2, 3, 4]

print(list1)
print(list2)
# in this case, list1 in last line makes a new referce variable. so, list2
# holds the previous assignment of list1.

# it works in this manner becase targets are mutable i.e. List in this case.