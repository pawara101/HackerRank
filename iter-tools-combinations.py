from itertools import combinations
[string,val] = input().split()
val = int(val)
CMB = []
combination_string=[]
for k in range(1,val+1):
    CMB = sorted(list(combinations(sorted(string),k)))
    #print(CMB)
    combination_string = combination_string+CMB


for i in combination_string:
    print(''.join(i))