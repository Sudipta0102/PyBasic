# Remove all of the vowels in a string

s = "don't be A stranger"
vowels = 'aeiouAEIOU'


s = ''.join([s[i] for i in range(len(s)) if s[i] not in vowels])

print(s)

