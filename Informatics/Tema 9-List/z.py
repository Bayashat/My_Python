#   https://informatics.mccme.ru/mod/statements/view.php?id=4163&chapterid=3853#1
a = list(input().split())
b = int(input())
b = b%len(a)

for i in a[-b:] + a[:-b]:
    print(i , end = ' ')