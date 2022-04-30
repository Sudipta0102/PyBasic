

test_list = [12, 67, 98, 34]

s = str(test_list[0])
sum = 0

for digit in s:
    sum += int(digit)

print(sum)


def sum_func(li):
    res = []
    for ele in li:
        sum=0
        for digit in str(ele):
            sum += int(digit)
        res.append(sum)
    return res


test_list = [12, 67, 98, 34]
print(sum_func(test_list))

