test_str = 'welcome to hell'

# s[:-1] -> picks up everything bt the last letter
# s[-1:] -> picks up the last letter
# title() method uppercase the first letter
#
li = test_str.title().split()

s0 = li[0][:-1]+li[0][-1:].upper()
s1 = li[1][:-1]+li[1][-1:].upper()
s2 = li[2][:-1]+li[2][-1:].upper()
print(str(s0+" "+s1+" "+s2))


# Now, same thing using lambda
# Access the last element using indexing.
# Capitalize the first word using title() method.
# Then join the each word using join() method.
# Perform all the operations inside lambda for writing the code in one-line.

def func(str):
    return ' '.join(map(lambda s: s[:-1]+s[-1:].upper(), str.title().split()))


test_str = 'welcome to hell'
print(func(test_str))
