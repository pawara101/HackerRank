s = 'HackerRank.com presents "Pythonist 2".'

def swap_case(s):

    swap_case = ''
    for i in range(0,len(s)):
        if s[i].isupper():
            swap_case = swap_case+(s[i].lower())
        elif s[i].islower():
            swap_case = swap_case+(s[i].upper())

        else:
            swap_case = swap_case+s[i]

    return swap_case

result = swap_case(s)
print(result)
