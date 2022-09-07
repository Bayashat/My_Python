n = int(input())
s = set()

def check(s):  # Aple25h
    flag = False

    for i in range(len(s)):
        if s[i].isupper():
            flag = True
            break
    if flag == True :
        flag = False
        for i in range(len(s)):
            if s[i].islower():
                flag = True
                break
        if flag == True:
            flag = False
            for i in range(len(s)):
                if s[i].isnumeric():
                    return True
        return False
    else:
        return False
    


for i in range(n):
    st = input()
    if check(st) == True:
        s.add(st)
l = list(s)
l.sort()
print(len(l))
for i in l:
    print(i)
