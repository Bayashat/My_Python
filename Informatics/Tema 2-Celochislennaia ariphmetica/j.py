"""
https://informatics.msk.ru/mod/statements/view.php?id=3309&chapterid=3464#1
Задача №3464. Сумма цифр
"""
a = int(input())
print((a % 10) + (a // 10 % 10) + (a // 100))


