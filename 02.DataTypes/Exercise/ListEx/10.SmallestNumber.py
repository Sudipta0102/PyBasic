list1 = [10, 20, 4]
# 1.
print(min(list1))
# 2.
list1.sort()
print(list1[0])
print(*list1[:1]) # i don't really understand this
# 3.
list2 = []

sizeoflist = int(input("Enter the size: "))

print("Enter elements:")
for ele in range(1, sizeoflist + 1):
    ele = int(input())
    list2.append(ele)

print(f"smallest element: {min(list2)}")


