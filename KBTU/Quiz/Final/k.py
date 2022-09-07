s = set(input().split())
l = []

def Power2(elem):
    while elem > 1:
        if elem%2 != 0:
            return False
        elem //= 2
    return True

for i in s:
    if Power2(int(i)):
        l.append(int(i))

l.sort()
for i in l:
    print(i, end = ' ')