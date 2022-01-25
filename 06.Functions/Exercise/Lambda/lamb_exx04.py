# problem statement: Given a list of numbers, write a Python program to count Even and Odd numbers in a List.

my_list = [2, 3, 1, 5, 3, 2, 6, 4, 8, 9]
even_filter_obj = filter(lambda x: x%2 == 0, my_list)
odd_filter_obj = filter(lambda x: x%2 != 0, my_list)

print("Even count:", len(list(even_filter_obj)))
print("Odd count:", len(list(odd_filter_obj)))


# also using list comprehension
even_count = len([x for x in my_list if x%2 == 0])
print(even_count)
