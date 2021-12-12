# use of __iter__() and __next__()

listB = ['Cat', 'Bat', 'Sat', 'Mat']

iter_listB = listB.__iter__()

while True:
    try:
        print(iter_listB.__next__())
    except:
        break