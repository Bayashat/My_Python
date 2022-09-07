l = input().split()
n = int(l[0]) # 4
x = int(l[1]) # 3

ls = []
for i in range(n):
    ls.append(2*i + x)

prod = 0
for i in ls:
    prod ^= i
print(prod)

