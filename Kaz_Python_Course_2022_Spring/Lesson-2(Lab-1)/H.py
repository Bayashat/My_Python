s = input()  # apple
c = input()   # e

cnt = s.count(c) # 1

if cnt == 1:
    print(s.find(c))

elif cnt >= 2:
    print(s.find(c), end = " ")
    print(s.rfind(c))