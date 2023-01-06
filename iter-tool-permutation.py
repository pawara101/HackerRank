from itertools import permutations
[string,val] = input().split()
val = int(val)

permutation_string = list(permutations(string,val))
permutation_string = sorted(permutation_string)
for i in permutation_string:
    print(''.join(i))