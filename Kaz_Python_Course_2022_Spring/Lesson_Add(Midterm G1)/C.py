n = int(input())

l = [int(x) for x in input().split()]

s = set(l)
l = list(s)

for i in range(len(l)): # 0-4
    print(i+1, l[i])