# 1. this is like a naive approach

def symmetry(s):
    n = len(s)
    flag = 0
    if n%2==1:
        mid=n//2+1
    else:
        mid=n//2

    start1=0
    start2=mid
    
    while(start1<mid and start2<n):
        if(s[start1]==s[start2]):
            start1+=1
            start2+=1
        else:
            flag = 1
            break
    
    if flag==1:        
        print(f"{s} is not symmetrical")        
    else:
        print(f"{s} is symmetrical")    

symmetry("khogkho")

# 2. Here, we can use slicing
def symmetry1(s):
    half = int(len(s)/2)
    if len(s)%2==1:
        first_half = s[:half]
        second_half = s[half+1:]
    else:
        first_half = s[:half]
        second_half = s[half:] 

    if(first_half==second_half):
        print(f"{s} is symmetrical")
    else:
        print(f"{s} is not symmetrical")                           


symmetry1("khogkhom")

