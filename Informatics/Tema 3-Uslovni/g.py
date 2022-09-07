"""
https://informatics.msk.ru/mod/statements/view.php?id=3380&chapterid=3507#1
Задача №3507. Сколько совпадает чисел
"""

a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
