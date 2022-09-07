"""
https://informatics.msk.ru/mod/statements/view.php?id=3309&chapterid=3472#1
Задача №3472. Конец уроков
"""

a = int(input())
a = a * 45 + (a // 2) * 5 + ((a + 1) // 2 - 1) * 15
print(a // 60 + 9, a % 60)
