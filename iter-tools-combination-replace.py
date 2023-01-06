from itertools import combinations_with_replacement
[string,val] = input().split()
val = int(val)
CMB = []
combination_string=[]


combination_string = sorted(list(combinations_with_replacement(sorted(string),val)))
for i in combination_string:
    print(''.join(i))