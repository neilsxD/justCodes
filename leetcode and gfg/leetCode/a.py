from math import ceil
tn = int(input())
lis = []
for _ in range(tn) : 
    lis.append(int(input()))

for el in lis:
    if el<=6 : print(15)
    else: 
        print(ceil(el/2)*5)




