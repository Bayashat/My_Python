from itertools import permutations

s = input()

def permut(s):  # abc  : 3! = 6 : abc acb bac bca cab cba
    for i in permutations(s):   # ('a', 'b', 'c')
        i = "".join(i)
        print(i)

permut(s)