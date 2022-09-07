"""
https://informatics.msk.ru/mod/statements/view.php?id=3309&chapterid=3467#1
Задача №3467. Парты
"""

a = int(input())
b = int(input())
c = int(input())
print(a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)