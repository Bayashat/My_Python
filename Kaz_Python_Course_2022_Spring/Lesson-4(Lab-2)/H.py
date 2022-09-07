import math

l = input().split()
x = int(l[0])
y = int(l[1])

n = int(input())

l = []
for i in range(n):
    l.append([])

k = 0
for i in range(n):
    q = input().split()
    x1 = int(q[0])
    y1 = int(q[1])
    l[k].append(x1)
    l[k].append(y1)
    k+=1

def my_func(l):
    return abs( math.sqrt( (l[0] - x)*(l[0] - x) + (l[1] - y)*(l[1] - y)) )
    
l.sort(key = my_func)

print(l)