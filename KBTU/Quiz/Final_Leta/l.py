s = input().split()

l = list()
for i in s:
    if s.count(i) == 1:
        l.append(i)

cnt = 0
for i in l:
    cnt += int(i)

print(cnt)