"""
https://informatics.msk.ru/mod/statements/view.php?id=3309&chapterid=3473#1
Задача №3473. Стоимость покупки
"""

a = int(input())
b = int(input())
n = int(input())

a *= n
b *= n
a += b//100
b = b%100
print(a, b)
