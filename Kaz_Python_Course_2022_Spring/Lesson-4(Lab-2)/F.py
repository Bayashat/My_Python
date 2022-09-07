dict = {}

n = int(input())
for i in range(n):
    l = input().split()
    s = l[0]
    x = int(l[1])
    if s in dict.keys():
        sum = dict[s] + x
        dict[s] = sum
    else:
        dict[s] = x

max = -1
for i in dict.values():
    if i > max :
        max = i

l = []
for i in dict.keys():
    l.append(i)
l.sort()

for i in l: 
    money = dict[i]
    money = max - money
    if money == 0:
        print(f'{i} is lucky!')
    else:
        print(f'{i} has to receive {money} tenge')

