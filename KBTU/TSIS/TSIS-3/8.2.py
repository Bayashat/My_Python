a = { int(i) for i in input().split()}
b = { int(i) for i in input().split() }

s = list(a.intersection(b))
s.sort()

for i in s:
    print(i, end = ' ')