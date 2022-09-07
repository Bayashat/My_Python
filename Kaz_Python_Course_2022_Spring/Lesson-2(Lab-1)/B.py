s = input()   # OK

def is_tasty(s):
    sum = 0
    for i in s:  # for(int i = 0; i < s.size(); i++)
        sum += ord(i)    # ord() функцисы берілген символдың аски таблицадағы мәнін береді

    if sum > 300:
        print("It is tasty!")
    else:
        print("Oh, no!")

is_tasty(s)

