def func(str):
    #str = 'aa'
    alplha_check = False
    num_check = False
    for ch in str:
        if ch.isalpha():
            alplha_check = True
        if ch.isnumeric():
            num_check = True

    return alplha_check and num_check


test_str = 'welcome2ourcountry34'
print(func(test_str))
