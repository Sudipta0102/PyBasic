dict1 = {3: 33, 2: 22, 4: 44, 1: 11, 0: 100}


#res = ()
for i in sorted(dict1):
    print(i, end = ' ')

print('\n\n')
for i in sorted(dict1):
    print(i, dict1.get(i), sep = ':', end='\n')

print('\n\n')
for i in sorted(dict1.keys()):
    print(i, dict1.get(i), sep=':', end='\n')

print('\n\n')
for i in sorted(dict1.keys()):
    print((i, dict1.get(i)), sep=':', end='\n')
