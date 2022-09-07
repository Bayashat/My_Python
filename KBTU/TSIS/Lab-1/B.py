s = input()

def Is_tasty(s):
    sum = 0
    for i in s:
        sum += ord(i)
    if sum > 300:
        print("It is tasty!")
    else:
        print("Oh, no!")
Is_tasty(s)
