import list

def cate(category):
    for i in list.movies:
        if i["category"] == category:
            print(i)

s = input()
cate(s)