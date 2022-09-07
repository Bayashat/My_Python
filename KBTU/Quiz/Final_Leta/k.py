a = [int(i) for i in input().split()] 
b = [int(i) for i in input().split()] 
c = list() 
for i in a: 
    if i not in b: 
        c.append(i) 
for i in b: 
    if i not in a: 
        c.append(i) 
c.sort() 
print(*c)