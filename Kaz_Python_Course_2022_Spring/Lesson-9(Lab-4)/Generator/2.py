
n = int(input())
result = [] # [0 2 4 6 8 10]

def Even_Gen(n): # 10 : 0,2,4,6,8,10
    for i in range(n+1):
        if i % 2 == 0:
            yield i

for x in Even_Gen(n):
    result.append(str(x))

print(','.join(result))