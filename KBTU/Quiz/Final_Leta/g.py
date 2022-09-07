n = int(input()) 
d = dict() 
s = set() 
for i in range(n): 
    a = input().split() 
    for j in range(1,len(a)): 
        if d.get(a[0],[])!=[]:d[a[0]].append(a[j]) 
        else:d[a[0]]=[a[j]] 
for i in d: 
    print(i + ": ", end = "") 
    print( *d[i], sep = ', ')