"""
https://informatics.msk.ru/mod/statements/view.php?id=3380&chapterid=3504#1
Задача №3504. Високосный год
"""

x = int(input())

if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
    print("YES")
else:
    print("NO")
