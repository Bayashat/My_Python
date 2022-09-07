"""
https://informatics.msk.ru/mod/statements/view.php?id=3380&chapterid=3509#1
Задача №3509. Ход ладьи
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print("YES" if (a == c or b == d) else "NO")