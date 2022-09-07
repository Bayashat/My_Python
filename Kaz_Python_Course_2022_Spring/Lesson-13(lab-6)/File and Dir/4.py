cnt = 0

with open("test.txt", "r") as f:
    while f.readline():
        cnt += 1

print(cnt)