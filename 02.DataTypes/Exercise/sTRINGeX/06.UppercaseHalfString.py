test_str = 'geeksforgeek'

print(len(test_str)/2)
# 1. using slicing.
# concatenating two parts of the string
s = test_str[:len(test_str)//2] + test_str[len(test_str)//2:].upper()

print(s)

half_idx = len(test_str) // 2

print(half_idx)

# 2. 
res = ''.join([test_str[idx].upper() if idx >= half_idx else test_str[idx]
               for idx in range(len(test_str))])

print(res)