"""
https://informatics.msk.ru/mod/statements/view.php?id=3380&chapterid=3503#1
Задача №3503. Знак числа
"""

x = int(input())

if x == 0:
    print(0)
else:
    print(1 if x > 0 else -1)
