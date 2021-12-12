s = "doremipasolatido"
for letter in s:
    if letter=='p':
        print()
        break
    else:
        print(letter, end=' ')
else:
    print("\nFor Else block")       

# here if, break gets executed, then for else block will not ne executed. 