"""
https://informatics.msk.ru/mod/statements/view.php?id=3309&chapterid=3477#1
Задача №3477. Улитка
"""

h = int(input())
a = int(input())
b = int(input())

i = 0
s = 0
while s <h:
    s += a
    if s >= h:
        i += 1
        break
    s -= b
    i += 1
print(i)
