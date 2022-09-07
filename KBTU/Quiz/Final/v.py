l = input().split()
a = int(l[0])
b = int(l[1])
c = int(l[2])
l2 = []

for i in range(1,a+1):
    if a%i==0 and b%i == 0:
        l2.append(i)


k = len(l2) - c
print(l2[k])