d1 = {1: "ami",2: "tumi", 3: 5, 5: "ami"}

# 1.
if 6 in d1:
    print('there')
else:
    print('Not there')

# 2. with try, exceot
try:
    print(d1[7])
except:
    print("bleh")
