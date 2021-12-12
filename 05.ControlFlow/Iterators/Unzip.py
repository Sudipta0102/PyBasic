# the reverse of zipping is unzipping.
# uses * operator with zip() function

l1, l2 = zip(*[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')])

print(l1)
print(l2)