# List features:
#  1. Third Bracket '[]'
#  2. can have duplicates
#  3. not ordered

a = ["apple", 'a', "bus", 'b', 4, 2.3, 'a']
b = [1,3,1,4,5,2,7,5,3]

print(a)
print(b)

a.remove("apple")
print(a)
print(a[4:9])

b.insert(3,"Apple")
print(b)

b.append("Bs")
print(b)

print(a[1].upper())

print(a)
a.reverse()
print(a)