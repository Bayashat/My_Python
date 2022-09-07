s = set(input().split())
l = []

def Palin(s):
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return True
        return False

for i in filter(Palin, s):
    l.append(i)

l.sort()
for i in l:
    print(i)

