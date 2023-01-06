from itertools import product
A = [int(x) for x in input().split()]  ## Gives multiple integer inputs in an array
B = [int(x) for x in input().split()]

prod = list(product(A,B))

for i in prod:
    print(i,end=" ")