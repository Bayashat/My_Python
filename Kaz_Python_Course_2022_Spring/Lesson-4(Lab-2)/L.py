brac = input() # ([])
l = [] # ()

for i in brac:
    if len(l) == 0:
        l.append(i)
    else:
        if (i == ')') & (l[len(l)-1] == '('):
            l.remove('(')
        elif (i == ']') & (l[len(l)-1] == '['):
            l.remove('[')
        elif (i == '}') & (l[len(l)-1] == '{'):
            l.remove('{')

if len(l) == 0:
    print("Yes")
else :
    print("No")
