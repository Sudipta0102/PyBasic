def revWords(s):
    words = s.split(" ")
    # reversing the whole list
    # then joining them by adding space
    revSen = ' '.join(reversed(words))
    print(revSen)

revWords("i am me")