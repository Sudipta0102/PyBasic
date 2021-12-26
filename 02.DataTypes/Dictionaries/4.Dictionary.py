# 1. uses second bracket, world call it curly braces
# 2. Dictionary is like map in java, key value pair
# 3. can not hold duplicate key, doesn't throw errors, but just doesn't keep the second one.
#    3a. wait a minute. point 3 has complication. Look at x.
#            if (there are same value with different keys && one of the aforementioned keys
#                       have duplicates with different values), then,
#                    One of the keys with same values will be replaced with the later value

# I need to phrase it better, i suck

x = {1:"ami",2:"tumi", 3: 5, 1: "sobai", 5: "ami"}

print(x)

y = {1:"ami",2:"tumi", 3: 5, 5: "ami"}

print(y)