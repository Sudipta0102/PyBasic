# Use a dictionary comprehension to count the length of each word in a sentence

s = "Don't be a stranger"
keys = [1, 2, 3, 4, 5, 6]
vals = ['a', 'b', 'c', 'd', 'e']

# dictionary comprehension
d1 = {k: v for k, v in zip(keys, vals)}
d2 = {k: k**2 for k in keys}
d3 = {char: ord(char) for char in 'coding'}
# ord() to get ascii value of a char.
d4 = {k: k**3 for k in keys if k**3 % 4 != 0}
d5 = {word: len(word) for word in s.split()}

print(d1)
print(d2)
print(d3)
print(d4)
print(d5)




# when you are done with this list, Go do the below list, you asshole...
# https://bbookman.github.io/Python-list-comprehension1/

