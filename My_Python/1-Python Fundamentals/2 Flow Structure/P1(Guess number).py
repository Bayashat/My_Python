"""                 P1. Guess number
  
The program will randomly generate a number from 1 to 100, and you need to guess that number.
If your guess is too big or too small, you will be prompted until you guess correctly

程序会随机生成一个1到100的数字, 你需要猜到那个数字.
如果你猜测的数字大了或小了, 会提示你, 直到猜对为止
"""
from random import randint

number = randint(1, 101)

guess = -1
while guess != number:
    guess = int(input("Enter your guess:  "))
    if guess > number:
        print("Your guess is too big")
    else:
        print("Your guess is too small")
else:
    print("Congratulations, you found it!!")
