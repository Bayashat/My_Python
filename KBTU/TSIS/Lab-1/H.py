s = input()
c = input()
cnt = s.count(c)

if cnt >= 2:
    print(s.find(c), end = " ")
    print(s.rfind(c))
elif cnt == 1:
    print(s.find(c))