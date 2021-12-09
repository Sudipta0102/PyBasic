import operator

# iadd()
a = 6
b = 3
print(operator.iadd(a, b)) # in place will not effective here

# iconcat()
s1 = "me"
s2 = "ew"
print(operator.iconcat(s1, s2)) # in place will not effective here

# isub()
print(operator.imul(a, b)) # in place will not effective here

# itruediv()
print(operator.itruediv(a, b))

# ifloordiv()
print(operator.ifloordiv(a, b))

# imod()
print(operator.imod(a, b))

# ixor()
print(operator.ixor(a, b))

# ipow()
print(operator.ipow(a, b))

# iand()
print(operator.iand(a, b))

# ior()
print(operator.ior(a, b))

# ilshift()
print(operator.ilshift(a, 1))

# irshift()
print(operator.irshift(a, 1))
