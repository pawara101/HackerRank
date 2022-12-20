def print_formatted(number):
    # your code goes here
    
   
    for i in range(1,number+1):

        thick = len(bin(number)[2:])
        print(

        str(i).rjust(thick," "),
        str(oct(i)[2:]).rjust(thick," "),
        str(hex(i)[2:].upper()).rjust(thick," "),
        str(bin(i)[2:]).rjust(thick," ")
        
        )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)