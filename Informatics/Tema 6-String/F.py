"""
https://informatics.msk.ru/mod/statements/view.php?id=3863&chapterid=3740#1
    Задача №3740. Второе вхождение
входные данные: comfort
выходные данные: -1

входные данные: coffee
выходные данные: 3
"""

s = input()  # coffee

if s.find('f') == -1:
    print(-2)
elif s.find('f') == s.rfind('f'):
    print(-1)
else:
    first = s.find('f')
    s = s.replace('f', 'x', 1)
    print(s.find('f'))
