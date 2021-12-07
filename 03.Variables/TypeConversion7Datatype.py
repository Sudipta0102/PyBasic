s = "lula"

t = tuple(s)
print(t)

t = list(s)
print(t)

t = set(s)
print(t)

a = 10

# convert a tuple of order (key,value) into a dictionary.
tup = (('a', [1,2]),('b', 'blast'),('c', 2))
c = dict(tup)
print(c)

# convert integer into a string
str = str(24)
print(str)

# converts real numbers to complex(real,imag) number.
complex = complex(1,2)
print(complex)