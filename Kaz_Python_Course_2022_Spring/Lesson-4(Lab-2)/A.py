from tkinter import N


l = input().split()  # 2 3 1 1 4
for i in range(len(l)):
    l[i] = int(l[i])



def check(number, index):  # 2 2
    if number > index:
        return True
    else:
        return False
jump = 0 # 

while jump != len(l):
    if (l[jump] == 0):
        for i in range(1,jump): # 2 1 
            if check(l[i], jump - i) == True:
                jump = i
                break
        print(0)
        
    else:
        jump += l[jump]
print(1)

