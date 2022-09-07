import datetime

y, m, d = input().split()  # 2000 01 01

day = datetime.date(int(y),int(m),int(d)) # 2000-01-01

today = datetime.date.today() # 2022-03-04

if day>today:
    print((day-today).days * 24 * 3600)

elif day<today:
    print((today - day).days * 24 * 3600)

elif day==today:
    print("0")