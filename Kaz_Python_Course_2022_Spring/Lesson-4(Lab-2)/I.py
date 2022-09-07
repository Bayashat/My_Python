n = int(input())
l = []
l2 = []

for i in range(n):
    x = input().split()
    if len(x) == 2:
        l.append(x[1])
    else:
        s = l.pop(0)
        l2.append(s)

for i in l2:
    print(i, end = " ")