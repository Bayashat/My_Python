n = int(input())

def down(n):
    while n >= 0:
        yield n
        n-=1

for x in down(n):
    print(x)