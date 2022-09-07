l = input().split()   # 1 2 3 1 4 2 5 3    : [1 2 3 4 5]

def unique(l):
    new_list = []

    for i in l:
        if i not in new_list:
            new_list.append(i)

    for i in new_list:
        print(i, end = ' ')
    
unique(l)