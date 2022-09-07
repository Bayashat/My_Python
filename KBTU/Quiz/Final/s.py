n = int(input())
l = input().split()

max = -1
for i in l:
    i = int(i)
    max = i if i > max else max

for i in l:
    i = int(i)
    if i == max:
        i = 1
        print(i, end = ' ')
    else:
        i = 0
        print(i, end = ' ')
