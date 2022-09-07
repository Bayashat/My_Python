import list

def aver_score(movies):
    average_score = 0.0
    sum = 0.0
    for i in movies:
        sum += i["imdb"]
    average_score = sum / len(movies)
    
    print(f"{average_score:.2f}")

aver_score(list.movies)

