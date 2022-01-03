# Find all of the numbers from 1–1000 that have a 6 in them


l1 = [x for x in range(6, 1001) if str(x).find('6') != -1]

print(l1)

