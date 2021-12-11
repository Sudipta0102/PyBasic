def OR(a, b):
    if a==1 or b==1:
        return True
    else:
        return False

# driver code
if __name__ == '__main__':
    print(" | OR Truth Table | Result |")
    print(" A = False, B = False | A AND B =",OR(False,False)," | ")
    print(" A = False, B = True | A AND B =",OR(False,True)," | ")
    print(" A = True, B = False | A AND B =",OR(True,False)," | ")
    print(" A = True, B = True | A AND B =",OR(True,True)," | ")
