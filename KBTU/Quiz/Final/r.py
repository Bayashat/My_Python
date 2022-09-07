c = input()
s = input()
l = []

for i in s:
    if i != c:
        l.append(i)
    
for i in l:
    print(i, end = '')