def func(a_list):

    a_list = [50, 60, 70]
    # a_list is now a local variable
    a_list.append(50)


my_list = [1, 2, 3]
print('my_list before func():', my_list)
func(my_list)
print('my_list after func():', my_list)