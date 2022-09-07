"""
https://informatics.msk.ru/mod/statements/view.php?id=3380&chapterid=3505#1
Задача №3505. Максимум трех чисел
"""

a = int(input())
b = int(input())
c = int(input())

if a>b:
  print(a if a>c else c)
else:
  print(b if b>c else c)