def func(a, b):
    flag = 0
    for i in a:
        for j in b:
            if i == j:
                flag = 1
                print(f"{i} is common")
                break
    if flag == 0:
        print("Nothing is common")


a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]

c = [1, 2, 3, 4, 5]
d = [6, 7, 8, 9]

e = [1, 2, 3, 4, 50, 9]

func(b, e)


# 2.converting into a set would be one more solution. because we can use intersection (&) to get the
# common values between two sets.
def has_common_elements(a, b):
    first = set(a)
    second = set(b)

    if first & second:
        return True
    else:
        return False


print(has_common_elements(c, d))


# 3. using set and intersection method.
def has_common_elements1(a, b):
    first = set(a)
    second = set(b)

    return len(first.intersection(second)) > 0


print(has_common_elements1(a, b))



