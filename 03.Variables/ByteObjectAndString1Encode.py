# some differences among many:
# 1. Byte objects are sequence of bytes and Strings are sequence of characters.
# 2. Byte Objects are in machine readable form and Strings are in human readable form.
# 3. That's why Byte objects are stored directly on the disk. But Strings need encoding
# before which they can stored on the disk.
# 
# 
# About Encoding:
# 1. PNG, JPEG, MP3, WAV, ASCII, UTF-8 etc aredifferent forms of encodings. 
# 2. Any text can be encoded to either UTF-8 or ASCII. 
# 3. Above can be achieved by encode(). default is 'UTF-8'. needs argument for ASCII.

# that's a string :D
a = "ToxicSelf"

# initialising a byte object
c = b"ToxicSelf"

d = a.encode() #UTF-8
e = a.encode('ASCII')

if(d==c and e==c):
    print("Encoding done")
else:
    print("Encoding effed")    

