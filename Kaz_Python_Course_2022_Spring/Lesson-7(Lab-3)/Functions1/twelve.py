l = [int(x) for x in input().split()]  # 1 2 3 4

def histogram(l):
    for i in l: # 3
        for j in range(i):
            print("*", end = "")
        print()

histogram(l)
