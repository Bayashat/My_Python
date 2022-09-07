n = int(input())
for i in range(n):
    x = int(input())
    if x <= 10:
        print("Go to work!")
    elif 10 <= x <= 25 :
        print("You are weak")
    elif 25 <= x <= 45:
        print("Okay, fine")
    else :
        print("Burn! Burn! Burn Young!")