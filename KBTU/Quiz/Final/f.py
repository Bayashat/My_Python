s = set(input().split())
s = [int(i) for i in s]
s2 = set()
def Power2(elem):
    if elem == 1: 
        return False
    while elem > 1:
        if elem%2 !=0:
            return True
        elem //=2
    return False

for elem in filter(Power2, s):
    s2.add(elem)

for i in s2:
    print(i, end = ' ')