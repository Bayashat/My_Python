a = int(input())
b = int(input())

def squares(a,b):
    for i in range(a,b+1):  # a~b
        yield i**2

for x in squares(a,b):
    print(x)