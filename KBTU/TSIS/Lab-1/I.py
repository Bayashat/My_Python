n = int(input())
for i in range(n):
    s = input()
    if s.find("@gmail.com") != -1:
        for i in s:
            if i == '@':
                break
            print(i, end = "")