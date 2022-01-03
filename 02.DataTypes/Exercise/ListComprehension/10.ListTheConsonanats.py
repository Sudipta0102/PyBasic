s = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"

vowels = 'aeiouAEIOU'

res = [cons for cons in s if cons not in vowels and cons != ' ']

print(res)


# find nums which has 3 in them.
nums = [num for num in range(1, 51) if str(num).find('3') != -1]
nums1 = [num for num in range(1, 51) if '3' in str(num)]
print(nums)
print(nums1)

