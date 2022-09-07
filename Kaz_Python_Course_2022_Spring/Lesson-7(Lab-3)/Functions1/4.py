def filter_prime(l):  # 1 2 3 4 5 6 7 8 9 : 2 3 5 7
    # Prime : 
    # 1. ( >= 2 )
    # 2. Only can divide 1 and its own  : 1 , itself
    for i in range(len(l)):
        if (l[i] >= 2) & check(l[i]):
            print(l[i], end = " ")


def check(x): # 5
    for i in range(2,x): # 2 3 4  
        if x % i == 0:
            return False

    return True    

l = [int(x) for x in input().split()]
filter_prime(l)