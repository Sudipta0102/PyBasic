
def multiplier_of(num1):
    def mul(num2):
        return num1*num2
    return mul


multiplywith5 = multiplier_of(5)
print(multiplywith5(9))