def func(s):
    words = s.split(' ')

    for word in words:
        if(len(word)%2==0):
            print(word)


func("me love python")
