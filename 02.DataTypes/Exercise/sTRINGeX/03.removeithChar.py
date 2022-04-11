# 1. Naive approach
# this is supposed to be o(n^2)...But I have no idea how
def removeith(s, index):
    new_str = ''
    for i in range(len(s)):
        if(i!=index):
            new_str = new_str + s[i]

    print(new_str)        

removeith("amamr", 0)    



# 2. we can use Slicing and concatenation technique
# this is supposed to be fastest of all
def removeith1(s, index):
    new_str = s[:index] + s[index+1:]
    print(new_str)

removeith1("pseudofunc", 0)

# Using List-compreshension
def removeith2(s, index):
    newStr = ''.join([s[i] for i in range(len(s)) if i!=index])
    print(newStr)

removeith2("imatret", 2)    
