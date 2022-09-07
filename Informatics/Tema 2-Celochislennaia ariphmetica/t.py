"""
https://informatics.msk.ru/mod/statements/view.php?id=3309&chapterid=3474#1
Задача №3474. Разность времен
"""

a1= int(input())
b1 = int(input())
c1 = int(input())

a2 = int(input())
b2 = int(input())
c2 = int(input())

s1 = a1*3600 + b1*60 + c1
s2 = a2 *3600 + b2*60 + c2
print(s2 - s1)