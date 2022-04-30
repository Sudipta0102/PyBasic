list1 = [12, -7, 5, 64, -14]

res = [ele for ele in list1 if ele >= 0]
print(res)

# using filter
pos_nos = list(filter(lambda x: (x >= 0), list1))
print(pos_nos)