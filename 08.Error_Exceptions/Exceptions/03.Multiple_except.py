def func(a):
    if a < 4:
        b = a/(a-3)

    print(f'value of b : {b}')


try:
    func(3)
    func(5)
except ZeroDivisionError:
    print('ZeroDivisionError occurred')
except NameError:
    print('NameError occurred')




