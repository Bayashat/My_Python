"""
https://informatics.msk.ru/mod/statements/view.php?id=3380&chapterid=3506#1
Задача №3506. Существует ли треугольник?
"""

a = int(input())
b = int(input())
c = int(input())

if (a + b) <= c or (a + c) <= b or (b + c) <= a:
    print("NO")
else:
    print("YES")
