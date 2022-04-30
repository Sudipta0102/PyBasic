list1 = [2, 7, 5, 64, 14]

# list comprehension
even_list = [ele for ele in list1 if ele % 2 == 0]
print(even_list)

# using lambda and filter
even_nos = list(filter(lambda x: (x % 2 == 0), list1))
print(even_nos)

