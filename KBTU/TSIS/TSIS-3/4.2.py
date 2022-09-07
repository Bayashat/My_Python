#   https://informatics.mccme.ru/mod/statements/view.php?id=4163&chapterid=3850#1
l =input().split()

n = l.count('0')

for i in filter(lambda x: x!='0' , l):
    print(i, end = ' ')

for i in range(n):
    print('0', end = ' ')