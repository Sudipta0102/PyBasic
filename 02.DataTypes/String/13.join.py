l1 = ['how', 'you', 'doin']

s1 = ' '.join(l1)

print(s1)

# above should be used as opposed to below:
s2 = ''
for i in l1:
    s2 += i + ' '

print(s2)
# this below operation is expensive to say the least.
# to quantify that we can derive the time behind that.

from timeit import default_timer as timer

l1 = ['a'] * 1000000

start = timer()
s2 = ''
for i in l1:
    s2 += i + ' '
stop = timer()
print(stop-start)

start = timer()
s1 = ' '.join(l1)
stop = timer()
print(stop - start)

