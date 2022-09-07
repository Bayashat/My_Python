"""
https://informatics.msk.ru/mod/statements/view.php?id=3309&chapterid=3481#1
Задача №3481. Часы
"""
x1 = int(input())  # 12: delayed hour
y1 = int(input())  # 34: delayed minute
a1 = int(input())  # 10: real hour relative to x1
b1 = int(input())  # 34: real minute relative to y1
x2 = int(input())  # 12: new delayed hour
y2 = int(input())  # 35: new delayed minute

tc = x1 * 60 + y1  # 754 : total minute of delayed
tr = a1 * 60 + b1  # 634 : total minute of time relative to (x1,x2)
tn = x2 * 60 + y2  # 755 : total minute of new delayed time

if tn < tr:
    tn = tn + 24 * 60
if tr < tc:
    tr = tr + 24 * 60  # 2074

raz = tr - tc  # 2074 - 754 = 1320
tnt = tc - raz  # -566
t = (tn - tnt) * 2  # 2642
rez = tnt + t  # 2076
a2 = (rez // 60) % 24  # 10
b2 = rez % 60  # 36
print(a2, b2)

