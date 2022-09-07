#   https://informatics.mccme.ru/mod/statements/view.php?id=4535&chapterid=3764#1

d = dict()

try:
    while True:
        Words = input().split()
        for word in Words :
            if d.get(word,0) !=0 : d[word] += 1
            else: d[word] = 1
except:
    pass

def f(item):
    return (-item[1], item[0])  # value-ді үлкеннен кішіге, ал key-ді кішіден үлкенге сорттау.

for item in (sorted(d.items(), key = f)):
    print(item[0])