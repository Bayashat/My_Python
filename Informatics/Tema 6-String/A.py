"""
https://informatics.msk.ru/mod/statements/view.php?id=3863#1
    Задача №3735. Делаем срезы
входные данные: Abrakadabra
выходные данные:
r
r
Abrak
Abrakadab
Arkdba
baaar
arbadakarbA
abdkrA
11
"""

s = input()  # Abrakadabra
length = len(s)

print(s[2])  # r
print(s[-2])  # r
print(s[:5])  # Abrak
print(s[:length-2])  # Abrakadab
print(s[::2])  # Arkdba
print(s[1::2])  # baaar
print(s[::-1])  # arbadakarbA
print(s[-1::-2])  # abdkrA
print(length)  # 11







