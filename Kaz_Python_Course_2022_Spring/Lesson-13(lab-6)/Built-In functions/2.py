s = input()  # Hello World   Up-2 Low-8 

cnt_up = 0
cnt_low = 0

for i in s:
    if i.islower():
        cnt_low += 1
    if i.isupper():
        cnt_up += 1

print(cnt_up)
print(cnt_low)

