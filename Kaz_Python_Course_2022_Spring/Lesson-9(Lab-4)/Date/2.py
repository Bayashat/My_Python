from datetime import date, timedelta
from functools import total_ordering
from time import time

today = date.today()

yesterday = today - timedelta(days = 1)

tommorrow = today + timedelta(days = 1)

print("Yesterday is : ", yesterday)
print("Today is : ",  today)
print("Tomorrow is : ",  tommorrow)