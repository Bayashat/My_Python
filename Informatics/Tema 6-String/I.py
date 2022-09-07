"""
https://informatics.msk.ru/mod/statements/view.php?id=3863&chapterid=3743#1
    Задача №3743. Дублирование фрагмента
Input: In the hole in the ground there lived a hobbit
Output: In the hole in the ground there lived a e hole in the ground there lived a hobbit
"""
s = input()

first = s[:s.find('h') + 1]  # In t
middle = s[s.find('h') + 1: s.rfind('h')]  # e hole in the ground there lived a
last = s[s.rfind('h'):]

print(first + middle + middle + last)

