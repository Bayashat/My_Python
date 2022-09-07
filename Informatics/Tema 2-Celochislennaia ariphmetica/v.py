"""
https://informatics.msk.ru/mod/statements/view.php?id=3309&chapterid=3476#1
Задача №3476. Дележ яблок - 3
"""

n = int(input())
k = int(input())

if k % n != 0:
    print(n - k % n)
else:
    print(0)
