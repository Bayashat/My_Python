"""
https://informatics.msk.ru/mod/statements/view.php?id=3380&chapterid=3508#1
Задача №3508. Тестирующая система
"""

x = input()
a = int(input())
if len(x) == 4:
    if x[0] == x[3] and x[1] == x[2]:
        print("YES" if a == 1 else "NO")
    else:
        print("YES" if a != 1 else "NO")
else:
    for i in range(4 - len(x)):
        x = "0" + x
    if x[0] == x[3] and x[1] == x[2]:
        print("YES" if a == 1 else "NO")
    else:
        print("YES" if a != 1 else "NO")
