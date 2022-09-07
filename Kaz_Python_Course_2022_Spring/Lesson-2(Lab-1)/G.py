'''
    <1> decimal to binary :
    12  ->  1100

    x = 12
    print(bin(x))


    <2>  Binary to decimal :
    1100 -> 12
    s = "1100"
    print(int(s,2))
'''
s = input()  # 1100
s = s[::-1]  # 0011

'''
def to_decimal(s):
    sum = 0
    degree = 0
    for i in s:
        sum += (2**degree) * int(i)
        degree+=1
    print(sum)
'''

def to_decimal(s, sum, degree, i):  # 0011, 12,  4, 4
    if i == len(s):
        return sum
    sum += (2**degree) * int(s[i])  # sum  = 12
    return to_decimal(s, sum, degree+1, i+1)

print(to_decimal(s, 0, 0, 0))