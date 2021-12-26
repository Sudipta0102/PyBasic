t1 = ("one")
print(type(t1)) # this is <class 'str'>
# but
t2 = ("one",)
print(type(t2)) # this is  <class 'tuple'> because of comma at the end

# ------------------------------------------------------------------

# the same goes for any other datatype inside a tuple like list
t3 = (['one', 2, 3])
print(type(t3))
# to access any element, just treat it like a normal list
print(t3[0])
# tuple is immutable, but in this case
t3[0] = 1
print(t3) # I can change because it's a list
t4 = (['one', 2, 3],)
print(type(t4))

# but if I use a tuple(). Then it's different story.

t1 = tuple("one")
print(type(t1)) # this is <class 'str'>
# but
t2 = tuple("one",)
print(type(t2)) # this is  <class 'tuple'> because of comma at the end
