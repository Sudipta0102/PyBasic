def func(start, end):
    res = [ele for ele in range(start, end+1) if ele % 2 == 0]
    return res


print(func(4, 16))


# by taking advantage of the python for loop
def func_another(start, end):
    for num in range(start, end+1, 2):
        print(num, end=" ")


func_another(4, 16)

