l = input().split()
s = 0
for i in range(len(l)):
    for j in range(i):
        if(l[i]==l[j]):
            s += 1
print(s)