coords = [(1,2), (15, 0), (7, 8), (4, 12)]

# in this case, by default it's sorted with every first element of the tuple.
sorted_coords_x = sorted(coords)

print(coords)
print(sorted_coords_x)

# let's say, we want to get the list sorted with the second element. For that,
# we can pass a lambda as key arg in sorted()
sorted_coords_y = sorted(coords, key=lambda x: x[1])
print(sorted_coords_y)


# also, not related to lambda but you can sort in a descending order by mentioning a reverse flag in sorted()
sorted_coords_y_descending = sorted(coords, key=lambda x: x[1], reverse=True)


# or let's say, you want to sort this based on the sum of tuple elements
sorted_coords_sum = sorted(coords, key=lambda x: x[0]+x[1])
print(sorted_coords_sum)
