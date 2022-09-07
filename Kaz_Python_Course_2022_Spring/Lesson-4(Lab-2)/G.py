Demon = int(input())
dict = {}
for i in range(Demon):
    l = input().split()  # [akaza, water]
    s = l[0]
    weakness = l[1]
    if weakness not in dict.keys():
        dict[weakness] = 1
    else :
        dict[weakness] += 1


Hunters = int(input())
for i in range(Hunters):
    l = input().split()  # [akaza, water, 10]
    s = l[0]
    ability = l[1]
    cnt = int(l[2])
    if dict[ability] <= cnt:
        dict[ability] = 0
    else:
        dict[ability] = dict[ability] - cnt

sum = 0
for i in dict.values():
    sum += i
print(f'Demons left: {sum}')