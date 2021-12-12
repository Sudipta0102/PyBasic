
def pyramidPrint(n):
    # this is for every row here
    for i in range(0, n):
        # this inner loop is to handle columns
        for j in range(0, i+1):
            print("* ", end = ' ')
        print()

pyramidPrint(5)        

# but above one is like emulating java code.

def pyramidPrint1(n):

    list = []
    for i in range(1, n+1):
        list.append("*"*i)
    print('\n'.join(list))
    
pyramidPrint1(5)

https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/

 needs to be revisited.

