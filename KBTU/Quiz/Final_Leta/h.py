n = int(input())
total = 0
l = list()

def my_func(s):
    cnt = 0
    for i in s:
        cnt+=1
    return cnt

l2 = list()
for x in range(0,n):
    s = input().split()

    for i in s:
        l.append(my_func(i))
    l.append(99999)

for x in l:
    if x == 99999:
        l2.sort()
        for j in l2:
            print(j, end=" ")
        l2.clear()
        print(f"total: {total}")
        total = 0
    else:
        l2.append(x)
        total += x
        