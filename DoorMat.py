N,M= map(int, input().split())

c = '.|.'
## Upper part
for i in range(1,N,2):
    print((i*c).center(M,'-'))

## Middle part
print('WELCOME'.center(M,'-'))

# lower part
for j in range(N-2,0,-2):
    print((j*c).center(M,'-'))