# try block to handle the exception
try:
    myList = []

    while True:
        myList.append(int(input()))

# if the input is non integer, it will just print the list
except:
    print(myList)
