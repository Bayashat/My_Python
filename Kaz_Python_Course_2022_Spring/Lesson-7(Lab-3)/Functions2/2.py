import list

l = []
def sublist(movies):
    for i in movies:
        if i["imdb"] > 5.5:
            l.append(i)

    print(l)


sublist(list.movies)