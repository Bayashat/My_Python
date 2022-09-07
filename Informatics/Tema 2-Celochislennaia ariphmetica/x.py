"""
https://informatics.msk.ru/mod/statements/view.php?id=3309&chapterid=3478#1
Задача №3478. Симметричное число
"""

x = input()
if len(x) == 4:
    if x[0] == x[3] and x[1] == x[2]:
        print(1)
    else:
        print(2)
else:
    for i in range(4 - len(x)):
        x = "0" + x
    if x[0] == x[3] and x[1] == x[2]:
        print(1)
    else:
        print(2)
