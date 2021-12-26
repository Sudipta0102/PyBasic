l_org = [1, 3, 2]

# 1. create an empty destination list and assign the original
# l_dest = []
l_dest = l_org

print(l_org)
print(l_dest)

l_dest.append(0)

print(l_org)
print(l_dest)
# see the problem ablove!!!. If we change the desination list then the Original list is changed too.
# That's because they are pointing to same reference.
# This is one case I have to be careful about.

# 2. using copy() function of list.
l_org = [1, 3, 2]

l_dest = l_org.copy()

print(l_org)
print(l_dest)


# 3. using list():
l_org = [1, 3, 2]

l_dest = list(l_org)

print(l_org)
print(l_dest)


# 4. using slicing. That is supposed to be faster than any of the above.
l_org = [1, 3, 2]

l_dest = l_org[:]
# [:] means copy first to last

print(l_org)
print(l_dest)


