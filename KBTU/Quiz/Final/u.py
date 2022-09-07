l = input().split()
h = int(l[0])
a = int(l[1])
b = int(l[2])

i = 0
s = 0
while s <h:
    s += a
    if s >= h:
        i += 1
        break
    s -= b
    i += 1
print(i)
