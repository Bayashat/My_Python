a,b = input().split('+')  # ONETWO + THR

transfer= {'ZER' : '0', 'ONE' : '1', 'TWO' :'2', 'THR' :'3', 'FOU' :'4',
'FIV' : '5', 'SIX' : '6', 'SEV' : '7', 'EIG' : '8', 'NIN' :'9' }

def z(s): # ONETWO
    y = ''#12
    for i in range(0,len(s)-1,3):
        x= s[i:i+3] # TWO
        y += transfer[x]
    return y

Y = str(int(z(a))+ int(z(b)))

for i in Y:
    for e1, e2 in transfer.items():
        if i==e2:
            print(e1, end='')

