n = int(input())

def square(n): # 5 : 1 2 3 4 
    for i in range(n):
        yield i**2

for x in square(n):
    print(x)