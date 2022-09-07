"""
https://informatics.msk.ru/mod/statements/view.php?id=3309&chapterid=3466#1
Задача №3466. Шнурки
"""

a = int(input())
b = int(input())
l = int(input())
n = int(input())
print((a*n)+(a*(n-1))+((b*(n-1))*2)+2*l)