def func(a_list):
    a_list[0] = 'changed'
    a_list[2] = 'changed'


my_list = [1, 2, 3]
print('my_list before func():', my_list)
func(my_list)
print('my_list after func():', my_list)