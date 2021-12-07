import file1

print("file2 __name__ = ", __name__)
if(__name__=='__main__'):
    print("file2 is being directly")
else:
    print("file2 is being imported")    