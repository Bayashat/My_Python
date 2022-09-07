n = int(input())

l = []

for i in range(n):
    l.append([])

for i in range(n):
    for j in range(n):
        l[i].append(j)

for i in range(n):
    l[0][i] = i
    l[i][0] = i
    
for i in range(1,n):
    for j in range(1,n):
        if i == j:
            l[i][j] = i*j
        else: l[i][j] = 0


for i in range(n):
    for j in range(n):
        print(l[i][j], end = " ")
    print()