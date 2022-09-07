"""
https://informatics.msk.ru/mod/statements/view.php?id=3309&chapterid=3475#1
Задача №3475. Автопробег
"""

a = int(input())
b = int(input())

if b % a == 0:
    print(b // a)
else:
    print(b // a + 1)
