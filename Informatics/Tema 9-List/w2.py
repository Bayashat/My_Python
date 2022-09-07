#   https://informatics.mccme.ru/mod/statements/view.php?id=4163&chapterid=3850#1
a = list(input().split())
n =a.count('0')

def f(elem):
    return elem != '0' 

for elem in filter(f,a):
    print(elem, end = ' ')
for i in range(n):
    print(0, end = ' ')