
def print_rangoli(size):
    import string
   

    l = list(string.ascii_lowercase[0:size])
    l_reverse = list(reversed(l))

    #print(l_reverse)


    ## Upper list
    for i in range(1,size+1):
        
        lst = l_reverse[:i]
        up_lst = lst+list(reversed(lst[0:i-1]))

        up_lst = '-'.join(up_lst)
        print(up_lst.center(4*size-3,'-'))

    ## Lower list
    for i in range(size-1,0,-1):
        
        lst = l_reverse[:i]
        up_lst = lst+list(reversed(lst[0:i-1]))

        up_lst = '-'.join(up_lst)
        print(up_lst.center(4*size-3,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)