test_list = [(4, 5, 5, 4), (5, 4, 3)]
K = 5
N = 2

for ele in test_list:
    if ele.count(K) == N:
        print(ele)
        break

res = [ele for ele in test_list if ele.count(K) == N]

print(res)

