"""
https://informatics.msk.ru/mod/statements/view.php?id=3309&chapterid=3469#1
Задача №3469. Электронные часы - 2
"""

n = int(input())
hours = n//3600 % 24

m1 = (n % 3600)//60//10
m2 = (n % 3600)//60 % 10

s1 = (n % 3600) % 60//10
s2 = (n % 3600) % 60 % 10

print(f'{hours}:{m1}{m2}:{s1}{s2}')
