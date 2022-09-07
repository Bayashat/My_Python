# https://informatics.mccme.ru/mod/statements/view.php?id=4535&chapterid=3750#1
a = {int(i) for i in input().split()}
b = {int(i) for i in input().split()}
print(len(a.intersection(b)))