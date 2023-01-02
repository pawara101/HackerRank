def merge_the_tools(string, k):
    
    def isUnique(arr):
        unique_list = []
        for i in arr:
            if i in unique_list:
                pass

            else:
                unique_list.append(i)

        return unique_list


    n = len(string)
    val = n//k
    string = list(string)
    
    ## Split the list
    spitted_list= []
    for i in range(0,n,k):
        spitted_list.append(string[i:i+k])

    print(spitted_list)

    l = len(spitted_list)

    for i in spitted_list:
        r = isUnique(i)
        r = ''.join(r)

        print(r)

    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)