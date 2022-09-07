s = input()

def is_palindrome(s): #  kazak
    for i in range(int( len(s)/2 ) ):
        if s[i] != s[len(s) - i - 1]:
            return False
        
    return True

if is_palindrome(s):
    print("It's a plindrome")
else:
    print("It's not a palindrome")