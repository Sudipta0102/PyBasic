def func(li, element):
    for ele in li:
        if ele == element:
            return True
        else:
            continue
    return False


test_list = [1, 6, 3, 5, 3, 4]
print(func(test_list, 10))

# gives you occurance of an element.
exist_count = test_list.count(3)
print(exist_count)
print(exist_count>0)
