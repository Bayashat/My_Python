n = int(input())
les = list()
for i in range(n):
    l = input().split()
    les.append(l)
k = 0
for i in les:
    k=0
    for j in i:
        print(len(j), end=" ")
        k += len(j)
    print("total:",k, end="\n")