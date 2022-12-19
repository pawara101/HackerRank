'''import textwrap
string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"

#print(textwrap.wrap(string,3))
print(textwrap.fill(string,5))'''
import textwrap

def wrap(string, max_width):
    wrap_text = textwrap.fill(string,max_width)
    return wrap_text

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)