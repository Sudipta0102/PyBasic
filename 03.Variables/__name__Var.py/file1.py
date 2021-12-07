# __name__ is a built-in variable which evaluates to the name of the current module. 

# so this __name__ var can be used to check whether the current module is being run 
# or being imported somewhere else. 

print("file1 __name__ =", __name__)

if __name__ == "__main__":
    print("file1 is being run directly")
else:
    print("file1 is being imported")    
