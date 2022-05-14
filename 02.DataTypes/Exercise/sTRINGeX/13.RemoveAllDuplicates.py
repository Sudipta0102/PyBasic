from collections import Counter, OrderedDict

s = "aaasssaaajjkksgherte"

# 1. COunter()
x = Counter(s).keys()

for i in x:
    print(i, end="")
print()

# 2. using set, but as set is an unordered collection, it's going to give you unordered string

x = "".join(set(s))
print(x)

# 3. using OrderedDict. This is going to give ordered string.
x = "".join(OrderedDict.fromkeys(s))
print(x)


