list2 = [70, 11, 20, 4, 100]
# firstly, need remove the largest element from the list and create another list
list3 = [ele for ele in list2 if ele<max(list2)]

print(list3)
print(max(list3))

# same thing can be achieved by iteration


def func(li):
    largest = li[0]
    secondlargest = li[0]
    # first get the largest
    for i in range(len(li)):
        if li[i] > largest:
            largest = li[i]

    #print(largest)

    for i in range(len(li)):
        if li[i] > secondlargest and li[i] != largest:
            secondlargest = li[i]

    print(secondlargest)


list2 = [70, 11, 20, 4, 100]
func(list2)

# 3. using sort we can achieve that
list3 = [70, 11, 20, 4, 100]
list3.sort()
print(list3[-2])


# also we can remove the largest element
list4 = [70, 11, 20, 4, 100]
list4.remove(max(list4))
print(max(list4))

