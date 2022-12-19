s = 'HackerRank.com presents "Pythonist 2".'

def swap_case(s):
    puncs = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    nums = '0123456789'
    swap_case = list()

    for i in range(0,len(s)):
        if ((s[i] in puncs) or (s[i] in nums) or (s[i].isspace())):
            swap_case.append(s[i])

        else:
            if s[i].isupper():
                swap_case.append(s[i].lower())
            if s[i].islower():
                swap_case.append(s[i].upper())

    swap_case = "".join(swap_case)
    #print(swap_case)

    return swap_case

result = swap_case(s)
print(result)
