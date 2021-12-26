# string to list with each word as the element of the string

s1 = 'how you doin'

l1 = s1.split()
# why it works? becaus the default argument of split is space
print(l1)

# can use other delimiter also or maybe a regex
s2 = 'how,you,doin'
l2 = s2.split(',')
print(l2)
