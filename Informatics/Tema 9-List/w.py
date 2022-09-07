#   https://informatics.mccme.ru/mod/statements/view.php?id=4163&chapterid=3850#1
a = list(input().split())
cnt = 0
for i  in range(len(a)):
    if a[i]!= '0':
        print(a[i], end = ' ')
    else:
        cnt += 1
while cnt!=0 : 
    print(0, end = ' ')
    cnt -= 1
