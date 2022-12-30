#has runtime error
s = input()

print(s)

name_split = s.split(" ")

print(name_split)
n = len(s.split(" "))
full_name =[]
for i in name_split:
    if i[0].islower():
        full_name.append(i.capitalize())

    print(full_name)



## Works well
def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s

print(solve(s))