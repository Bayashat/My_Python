"""
https://informatics.msk.ru/mod/statements/view.php?id=3863&chapterid=3742#1
    Задача №3742. Обращение фрагмента
входные данные: In the hole in the ground there lived a hobbit
выходные данные: In th a devil ereht dnuorg eht ni eloh ehobbit
"""
s = input()

first = s[:s.find('h') + 1]  # In t
middle = s[s.find('h') + 1: s.rfind('h')]  # e hole in the ground there lived a
last = s[s.rfind('h'):]

print(first + middle[::-1] + last)