def func(test_list, letter):
    res = []
    for s in test_list:
        for s1 in s.split():
            if s1.lower().startswith(letter):
                res.append(s1)
    return res


li = ["Gfg is best", "Gfg is for geeks", "I love G4G"]
print(func(li, 'g'))

# list comprehension

res = [s1 for s in li for s1 in s.split() if s1.lower().startswith('g')]
print(res)

