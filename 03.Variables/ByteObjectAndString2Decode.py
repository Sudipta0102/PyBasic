# Byte objects to String can be achieved by decode()

# Initialising a string
a = "ToxicSelf"

# Initialising a byte object
c = b"ToxicSelf"

# to decode the byte object to String
d = c.decode() # default is UTF-8
e = c.decode('ASCII')

if(a==d and a==e):
    print("decoding Successful.")
else:
    print("Decoding effed.")    