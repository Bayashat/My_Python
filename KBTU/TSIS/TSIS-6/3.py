def multiple_list(x:list):
    r = 1
    for i in x:
        r *= i
    return r

l = [1,2,3,4,5]
print(multiple_list(l)) # 120