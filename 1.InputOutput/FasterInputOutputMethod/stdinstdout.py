# 1. sys.stdin is a File object.
#    it's like creating any other file object to read input from the file. 
#    But in this case, the file will be stansdard input buffer.
# 2. stdout('D\n') is always fater than print('D')
# 3. if we write all the things at once, it will be even faster apparently.
#    (example: "".join(list-comprehension))

from sys import stdin, stdout


def main():
    n = stdin.readline()

    arr = [int(x) for x in stdin.readline().split()]

    sum = 0

    # here could use in-built sum(arr)
    for x in arr:
        sum+=x

    # this write() method can only perform string operation that's why str(sum) 
    print(str(sum))

def main1():
    n = int(input("Enter size: "))

    arr = [int(nums) for nums in input("Enter numbers: ").split()]

    print("sum:",sum(arr))

    

if __name__ == '__main__':
    main1()


# important note: There are more ways to make it faster. But Not now 
# I am going to do it. Here's link for later:
# https://www.geeksforgeeks.org/python-input-methods-competitive-programming/


