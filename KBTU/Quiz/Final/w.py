l = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

s = input()

for i in range(len(l)):
    if l[i] == s:
        print(len(l) - i)