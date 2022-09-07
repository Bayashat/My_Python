"""
https://informatics.msk.ru/mod/statements/view.php?id=3380&chapterid=3502#1
Задача №3502. Какое число больше?
"""

a = int(input())
b = int(input())
if a == b:
    print(0)
else:
    print(1 if a > b else 2)
