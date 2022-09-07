import math

k = -1
l = []

while k != 0:
    k = int(input())
    l.append(k)

l.remove(0)

if len(l)%2 == 0:
    for i in range(int(len(l) / 2)): 
        print(l[i] + l[len(l) - i - 1], end = " ")
else:
    for i in range(int(len(l) / 2)): 
        print(l[i] + l[len(l) - i - 1], end = " ")
    print(l[int(len(l) / 2)])  
