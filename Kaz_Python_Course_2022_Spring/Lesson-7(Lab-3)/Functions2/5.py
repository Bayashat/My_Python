import list

s = input()


def average(s):
    sum = 0.0
    cnt = 0
    for i in list.movies:
        if i["category"] == s:
            sum += i["imdb"]
            cnt += 1
    
    average_score = sum / cnt

    print(f"{average_score:.2f}")

average(s)