n = int(input())

x = 1 
if n % 2 == 0:
    for i in range(n):     
        for j in range(x):
            print("#", end = "")
        for i in range(n - x):
            print(".", end = "")
        x += 1
        print()

else:
    for i in range(n):     
        for j in range(n-x):
            print(".", end = "")
        for i in range(x):
            print("#", end = "")
        x += 1
        print()
