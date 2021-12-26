l = [2, 1, 5, -1, -6, 2, 9, 4]
print(l)

# list has sort method which is in place sorting. Like this:
l.sort()

print(l)


# To not to do in place sort, use sorted(), like this:

l = [2, 1, 5, -1, -6, 2, 9, 4]

sorted_l = sorted(l)

print(l)
print(sorted_l)

# to achieve descending sorting, use the reverse flag. Like this:
l = [2, 1, 5, -1, -6, 2, 9, 4]

l.sort(reverse=True)

print(l)

# same reverse flag in sorted() too.
l = [2, 1, 5, -1, -6, 2, 9, 4]

sort_l = sorted(reverse=True) # this didn't work, says need more param.

print(sort_l)


