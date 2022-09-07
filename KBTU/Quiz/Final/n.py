a = input()
b = input()
l1 = []
l2 = []

for i in a:
    l1.append(i)

for i in b:
    l2.append(i)

l1.sort()
l2.sort()

x = 0

if len(l1) != len(l2):
    x = 1
for i in range(min(len(a), len(b))):
    if l1[i] != l2[i]:
        x = 1
        break
print("YES" if x == 0 else "NO")