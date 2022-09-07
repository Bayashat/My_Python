d = {}
try:
    while True:
        Txt = input().split()
        for i in Txt:
            if d.get(i, 0) == 0:
                d[i] = 1
            else:
                d[i] += 1
except:
    pass

d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
for i in d:
    print(i[0])
