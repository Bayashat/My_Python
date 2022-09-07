l = input().split()

s2 = set()
l3 = list()
l.sort()

for i in l:
    s2.add(i)
s2 = list(s2)
s2.sort()

for i in s2:
    l3.append(l.count(i))

for i in range(0,len(s2)):
    print(f"{s2[i]} - {l3[i]}")
    