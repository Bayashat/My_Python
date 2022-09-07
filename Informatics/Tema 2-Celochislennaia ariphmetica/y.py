"""
https://informatics.msk.ru/mod/statements/view.php?id=3309&chapterid=3479#1
Задача №3479. Проверьте делимость
"""

a = int(input())
b = int(input())

if a % b == 0 or b % a == 0:
    print(1)
else:
    print(2)
