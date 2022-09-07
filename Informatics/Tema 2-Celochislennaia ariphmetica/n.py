"""
https://informatics.msk.ru/mod/statements/view.php?id=3309&chapterid=3468#1
Задача №3468. Электронные часы - 1
"""

n = int(input())
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, minutes)