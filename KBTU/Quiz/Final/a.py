import math

Q = input().split()
A = int(Q[0])
B = int(Q[1])

l = list()

def Power3(elem):
    if elem == 1: 
        return False
    while elem > 1:
        if elem%3 !=0:
            return False
        elem //= 3
    return True

x = A
while x != B:
    if Power3(x):
        l.append(x)
    x += 1

l = [str(i) for i in l]
l2 = []
for i in l:
    if len(i) == 4:
        l2.append(int(i))
l2.sort(reverse=True)
for i in l2:
    print(i, end = ' ')