a = input().split()
a.sort()

value = int(input())

mid = len(a) // 2
l = 0
r = len(a) - 1

while int(a[mid]) != value and l <= r :
    if a[mid] == value :
        break
    if value > int(a[mid]):
        l = mid + 1
    else :
        r = mid - 1
    mid = (l+r) // 2
if l >r :
    print('no')
else :
    print(mid)