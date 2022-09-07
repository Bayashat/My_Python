"""
https://informatics.msk.ru/mod/statements/view.php?id=3863&chapterid=3739#1
    Задача №3739. Первое и последнее вхождение
входные данные: comfort
выходные данные: 3

входные данные: office
выходные данные: 1 2
"""

s = input()  # office

if s.find('f') == -1:
    print()
elif s.find('f') == s.rfind('f'):
    print(s.find('f'))
else:
    print(s.find('f'), s.rfind('f'))