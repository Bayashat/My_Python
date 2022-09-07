s = input()   # Hello

s2 = reversed(s)

if list(s) == list(s2):  # 
    print("Yes, it's Palindrome")
else:
    print("NO")