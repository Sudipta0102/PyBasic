# finding power using recursion

def mfunc(num, power):
    if power == 0:
        return 0

    if power == 1:
        return num

    return num * mfunc(num, power - 1)


if __name__ == '__main__':
    print(mfunc(5, 3))
