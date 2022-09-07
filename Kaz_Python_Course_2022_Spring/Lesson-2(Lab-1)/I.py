n = int(input())

for i in range(n):
    s = input()
    if s.find("@gmail.com") != -1:    # 1234abcd@gmail.com
        for i in s :  # for(int i = 0; i < s.size(); i++)
            if i == '@':
                print()
                break
            print(i, end = "")