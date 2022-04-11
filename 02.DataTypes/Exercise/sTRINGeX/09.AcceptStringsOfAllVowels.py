import re

# logic is, if the character is successfully added to the set which consists of only vowels...
# that means the character is other than vowels. Hence, not accepted.

def func(str):
    #str = 'aa'
    set_of_vowels = set('aeoiu')
    print(set_of_vowels)
    print(len(set_of_vowels))
    for ch in str:
        set_of_vowels.add(ch)

    if len(set_of_vowels) == 5:
        print('Accepted')
    else:
        print('Not Accepted')


def func_regex(str):
    c = re.compile("[^aeiouAEIOU]")
    if len(c.findall(str)) > 0:
        print('Not Accepted')
    else:
        print('Accepted')


if __name__ == '__main__':
    func_regex('aaan')