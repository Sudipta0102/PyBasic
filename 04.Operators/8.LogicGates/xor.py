def XOR(a, b):
    if (a!=b):
        return True
    else:
        return False 


# driver code
if __name__ == '__main__':
    print(" | XOR Truth Table | Result |")
    print(" A = False, B = False | A AND B =",XOR(False,False)," | ")
    print(" A = False, B = True | A AND B =",XOR(False,True)," | ")
    print(" A = True, B = False | A AND B =",XOR(True,False)," | ")
    print(" A = True, B = True | A AND B =",XOR(True,True)," | ")        