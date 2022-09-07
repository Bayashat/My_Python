import random

name = input("Hello! What is your name?\n")

print(f"Well, {name}, I am thinking of a number between 1 and 20.")
print("Take a guess.")
x = random.randint(1,20)

user_number = 0
cnt = 0

while(user_number != x):
    user_number = int(input())
    if user_number < x:
        cnt+=1
        print("Your guess is too low.\nTake a guess.")
    elif user_number > x :
        cnt+=1
        print(("Your guess is too big.\nTake a guess."))
    else:
        cnt+=1
        print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
    


