"""
https://informatics.msk.ru/mod/statements/view.php?id=3863&chapterid=3738#1
    Задача №3738. Переставить два слова
входные данные: Hello, world!
выходные данные: world! Hello,
"""

s = input()  # hello world

index = s.index(' ')  # 5: the index of space

s1 = s[index+1:]  # second word
s2 = s[:index]  # first word
print(s1 + ' ' + s2)  # world hello

