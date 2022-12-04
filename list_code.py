if __name__ == '__main__':
    N = int(input())
    numberList = list()
    useriInputs = list()

    for inputs in range(0,N):
        #Input types  - append,insert,print
        useriInputs = input().split()

        if useriInputs[0] == 'append':
            numberList.append(int(useriInputs[1]))
            #print(numberList)

        elif useriInputs[0] == 'insert':
            insertInt = int(useriInputs[2])
            insertIndex = int(useriInputs[1])

            if len(numberList)==0 or len(numberList)==insertIndex:
                numberList.append(insertInt)
            else:
                numberList.insert(insertIndex,insertInt)

        elif useriInputs[0] == 'remove':
            removeInteger = int(useriInputs[1])
            numberList.remove(removeInteger)

        elif useriInputs[0] == 'sort':
            numberList.sort()

        elif useriInputs[0] == 'reverse':
            numberList.reverse()

        elif useriInputs[0] == 'pop':
            numberList.pop()

        elif useriInputs[0]=='print':
            print(numberList)

        else:
            print('repeat again')

        #print(numberList)
    
    #lst1 = [item for item in input("Enter the list items : ").split()]
    