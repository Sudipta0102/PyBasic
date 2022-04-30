test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

res = ", ".join(test_list)
print(res)

res = res.replace("G", "_").replace("e", "G").replace("_", "e")
print(res)
