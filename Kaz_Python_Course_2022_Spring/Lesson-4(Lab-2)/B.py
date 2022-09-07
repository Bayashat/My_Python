n = int(input())
l = input().split()

for i in range(len(l)):
    l[i] = int(l[i])

l.sort() # 1 2 5 7
l.reverse() # 7 5 2 1
print(l[0] * l[1])


