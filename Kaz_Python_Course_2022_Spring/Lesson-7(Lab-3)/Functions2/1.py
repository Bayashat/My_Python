import list

def check(movie):
    if movie["imdb"] > 5.5:
        return True

    else:
        return False

if check(list.movies[7]):
    print("True")
else: print("False")
