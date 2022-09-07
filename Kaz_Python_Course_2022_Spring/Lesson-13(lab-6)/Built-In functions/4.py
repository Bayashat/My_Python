from time import sleep
import math


number = int(input())
milli_sec = int(input())  # 

sleep(milli_sec / 1000)

sq = math.sqrt(number)
print(f"Square root of {number} after {milli_sec} miliseconds is {sq}")