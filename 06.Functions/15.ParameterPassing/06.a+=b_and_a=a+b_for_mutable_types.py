# another example with rebinding references.
def func1(a_list):
    # this is supposed to change the outer variable
    a_list += [4, 5]


def func2(a_list):
    # this rebinds the reference to a new local variable
    a_list = a_list + [4, 5]


my_list = [1, 2, 3]
print('my_list before func1():', my_list)
func1(my_list)
print('my_list after func1():', my_list)


my_list = [1, 2, 3]
print('my_list before func2():', my_list)
func2(my_list)
print('my_list after func2():', my_list)