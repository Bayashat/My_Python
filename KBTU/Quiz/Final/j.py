Q = list(input().split())
x = int(Q[0])
l = []


def Prime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


while x != int(Q[1]):
    if Prime(x):
        l.append(x)
    x += 1
l.sort(reverse=True)
for i in l:
    print(i, end=' ')
