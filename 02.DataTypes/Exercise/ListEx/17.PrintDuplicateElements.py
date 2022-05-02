li = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

res = []
for num in li:
    if li.count(num) > 1 and res.count(num) == 0:
        res.append(num)

print(res)

