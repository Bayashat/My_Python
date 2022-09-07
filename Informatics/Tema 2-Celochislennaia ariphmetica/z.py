"""
https://informatics.msk.ru/mod/statements/view.php?id=3309&chapterid=3480#1
Задача №3480. Максимум
"""

x = int(input())
y = int(input())

z = ((x - y) ** 2) ** 0.5  # z: бұл x және y тің айырмасы. Бірақ кей жағдайда ол теріс сан шығуы мүмкін, сондықтан
# квадраттап,түбір астына аламыз

result = int( (x + y + z) / 2)
print(result)
