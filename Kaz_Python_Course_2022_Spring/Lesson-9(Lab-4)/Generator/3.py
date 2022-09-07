n = int(input())

def check(n):
    for i in range(1,n):
        if((i%3==0) & (i%4==0)):
            yield i 

for x in check(n):
    print(x)