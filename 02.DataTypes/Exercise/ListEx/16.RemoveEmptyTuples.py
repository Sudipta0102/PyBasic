tuples_list = [(), ('ram','15','8'), (), ('laxman', 'sita'),
                  ('krishna', 'akbar', '45'), ('',''),()]


li = [t for t in tuples_list if t] # i don't understand this why "if t"
print(li)

li2 = list(filter(None, tuples_list))
print(li2)

li3 = [t for t in tuples_list if t != ()]
print(li3)