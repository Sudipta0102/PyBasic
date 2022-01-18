def mfunc(*args, **kwargs):
    for arg in args:
        print(arg, end =' ')
    print()
    for key in kwargs:
        print(key, kwargs[key],sep=':', end='  ')
    print()


mfunc([1, 2, 4], 'hamborai', 'helpulice', 'hapus-hupus', first_name='Pseudo', last_name='func')
