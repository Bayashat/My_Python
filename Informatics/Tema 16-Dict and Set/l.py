#   https://informatics.mccme.ru/mod/statements/view.php?id=4535&chapterid=3760#1
n = int(input())
d = {}
for i  in range(n):
    one,two = input().split()
    d[one] = two
    d[two] = one
print(d[input()])