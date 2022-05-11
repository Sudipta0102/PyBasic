# 1. this is the naive approach
#  
def palindrome(s):
    n = len(s)
    flag = 0

    # need to find the mid
    if n % 2 == 1:
        mid = n // 2 + 1
    else:
        mid = n // 2

    start1 = 0
    start2 = n - 1

    while start1 < mid < start2:
        if s[start1] == s[start2]:
            start1 += 1
            start2 -= 1
        else:
            flag = 1
            break

    if flag == 1:
        print(f"{s} is not palindrome")
    else:
        print(f"{s} is palindrome")


palindrome("amiimaa")


# 2. One can use slicing approach
def palindrome1(s):
    half = int(len(s) / 2)

    if len(s) % 2 == 0:
        first_half = s[:half]
        second_half = s[half:]
    else:
        first_half = s[:half]
        second_half = s[half + 1:]

    # finding out reverse of second_half string using slicing technique again
    if first_half == second_half[::-1]:
        print(f"{s} is palindrome")
    else:
        print(f"{s} is not palindrome")


palindrome1("amiima")
