l = input().split()  # ['13', '24']
n = int(l[0])  # 13
k = int(l[1])  # 24

def is_good(x):
    if x < 500:
        # prime number : 1-ге және өзіне ғана бөлінеді
        '''
        c++ version : 
        for(int i = 2; i < x; i++) # 7 : 2-6
        {
            if(x % i == 0)
            {
                return False
            }
        }
        '''
        for i in range(2,x):
            if x % i == 0:
                return False
        return True
    else:
        return False

if (is_good(n) == True) & (k % 2 == 0):
    print("Good job!")
else:
    print("Try next time!")



