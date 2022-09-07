import math

x = int(input())
l = []


def Seven(x):
    while x != 0:
        l.append(x % 7)
        x //= 7
    return l


l = Seven(x)

sum = 0
ll = []
q = 0
for i in range(len(l) - 1, -1, -1):
    if i == len(l) - 1:
        q = l[i] * pow(10, len(l) - 1)
        sum += q
    else:
        q = q // 10
        sum += l[i] * q

print(sum)

# 45045: 24634
