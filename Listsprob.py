
N = 2
numList = list()
input_List = list()
for inp in range(N):
    x = [x for x in input().split()]
    input_List.append(x)

    print(x[0])

    if x[0] == 'insert':
        pos,num = x[1],x[2]
        print(x[1])
        print(x[2])
        numList.append(x[2])

    if x[0] == 'print':
        print(numList)


