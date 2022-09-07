n = int(input()) # 3 : 5 25 45
for i in range(n):  # 0 1 2  for(int i = 0; i < n; i++)
    x = int(input())
    if x <= 10:
        print("Go to work!")
    elif 10<=x<=25 :
        print("You are weak")
    elif 25<=x<=45:
        print("Okay, fine")
    else :
        print("Burn! Burn! Burn Young!")


