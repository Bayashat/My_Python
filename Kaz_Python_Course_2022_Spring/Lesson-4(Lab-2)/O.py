text = input() # ONETWO+THR

s = ""
s2 = ""
st = "" # 
st2 = ""
flag = False
for i in range(len(text)):
    
    if flag == True :
        s2 += text[i]
        if len(s2) == 3:
            if s2 == "ONE":
                st2 += '1'
            elif s2 == "TWO":
                st2 += '2'
            elif s2 == "THR":
                st2 += '3'
            elif s2 == "FOU":
                st2 += '4'
            elif s2 == "FIV":
                st2 += '5'
            elif s2 == "SIX":
                st2 += '6'
            elif s2 == "SEV":
                st2 += '7'
            elif s2 == "EIG":
                st2 += '8'
            elif s2 == "NIN":
                st2 += '9'
            elif s2 == "ZER":
                st2 += '0'
            s2 = ""
    else:
        if text[i] == '+':
            flag = True
            continue
        
        s += text[i]
        if len(s) == 3:
            if s == "ONE":
                st += '1'
            elif s == "TWO":
                st += '2'
            elif s == "THR":
                st += '3'
            elif s == "FOU":
                st += '4'
            elif s == "FIV":
                st += '5'
            elif s == "SIX":
                st += '6'
            elif s == "SEV":
                st += '7'
            elif s == "EIG":
                st += '8'
            elif s == "NIN":
                st += '9'
            elif s == "ZER":
                st += '0'
            s = ""

sum = int(st) + int(st2)
string = str(sum) # "579"
s = ""
for i in string :
    if i == '0':
        s += "ZER"
    if i == '1':
        s += "ONE"
    if i == '2':
        s += "TWO"
    if i == '3':
        s += "THR"
    if i == '4':
        s += "FOU"
    if i == '5':
        s += "FIV"
    if i == '6':
        s += "SIX"
    if i == '7':
        s += "SEV"
    if i == '8':
        s += "EIG"
    if i == '9':
        s += "NIN"
print(s)
    
