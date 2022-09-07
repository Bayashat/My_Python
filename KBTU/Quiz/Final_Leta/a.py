from collections import defaultdict

d = defaultdict(list)
d={}

n=int(input())

for i in range(n):
    a,b = input().split()

    d.setdefault(a,[]).append(int(b))

sm=0
k=0

for i in d:
    for j in d[i]:
        sm+=int(j)
        k+=1
    res = sm / k
    d[i] = res
    res = 0
    sm = 0
    k=0

for key, value in sorted(d.items()):
    s = key+":"
    print(s,f'{d[key]:.3f}')