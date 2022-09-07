"""
https://informatics.msk.ru/mod/statements/view.php?id=3863&chapterid=3741#1
    Задача №3741. Удаление фрагмента
входные данные: In the hole in the ground there lived a hobbit
выходные данные: In tobbit
"""

s = input()

first = s.find('h')
last = s.rfind('h')

between_s = s[first: last + 1]
s = s.replace(between_s, '')
print(s)

"""
s = input()
s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)
"""