s = input().split()
n = int(s[0])
k = int(s[1])

def is_true(n):
    if n < 500:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    else:
        return False

if (is_true(n) == True) & (k%2==0):
    print("Good job!")
else:
    print("Try next time!")