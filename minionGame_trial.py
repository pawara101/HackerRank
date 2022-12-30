vowels = ['A','E','I','O','U']

string_vow = list()
string_cos = list()
string = 'BANANA'
string = list(string)
for i in string:
    if(i in vowels):
        string_vow.append(i)

    else:
        string_cos.append(i)

#print(string_vow)
#print(string_cos)

sub_str=list()
## For Stuart


string_copy = string.copy()
ind = [ind for (ind,i) in enumerate(string) if i in string_cos]

#print(ind)

## Stuart ##
count_st=0
for i in ind:
    for j in range(i,len(string)):
        #print(string[i:j+1])
        count_st = count_st+1

print(count_st)


## Kevin ##
ind = [ind for (ind,i) in enumerate(string) if i in string_vow]
count_kv=0
for i in ind:
    for j in range(i,len(string)):
        #print(string[i:j+1])
        count_kv = count_kv+1

print(count_kv)


if count_kv > count_st:
    print(f'Kevin {count_kv}')


else:
    print(f'Stuart {count_st}')

