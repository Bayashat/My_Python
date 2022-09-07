"""
https://informatics.msk.ru/mod/statements/view.php?id=3863&chapterid=3737#1
    Задача №3737. Две половинки
входные данные: Hi
выходные данные: iH

входные данные: Hello
выходные данные: loHel
"""

s = input()  # hello
length = len(s) + 1  # 6
s1 = s[: length // 2]  # Hel
s2 = s[length // 2:]  # lo
print(s2 + s1)
