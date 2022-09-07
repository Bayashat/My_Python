# https://informatics.mccme.ru/mod/statements/view.php?id=4535&chapterid=3751#1
a = {int(i) for i in input().split()}
b = {int(i) for i in input().split()}

c  = list(a.intersection(b))
c.sort()

for i in range(c):
    print(c[i], end = ' ')

# for i in c:
#    print(i,end =' ')