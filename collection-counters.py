from collections import Counter
X = int(input())
Shoe_list = [int(x) for x in input().split()]
N = int(input())

customer = []
for i in range(N):
    [shoe_size ,val ] = [int(x) for x in input().split()]
    customer.append([shoe_size ,val ])

# print(X)
# print(Shoe_list)
# print(N)
# print(customer)

shoe_detail = Counter(Shoe_list)
shoe_size_detail = shoe_detail.keys()
shoe_quantity = shoe_detail.values()

# print(shoe_detail)
# print(shoe_size_detail)
# print(shoe_quantity)


total = 0
for i in customer:

    if (i[0] in shoe_detail) and (shoe_detail[i[0]]>0):

        total = total + i[1]
        shoe_detail[i[0]] = shoe_detail[i[0]] - 1


print(total)