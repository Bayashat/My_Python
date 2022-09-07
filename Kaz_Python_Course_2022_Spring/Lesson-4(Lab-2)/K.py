text = input()  # Hello, 

for i in range(len(text)):
    if (ord(text[i]) >= 33) & (ord(text[i]) <= 63):
        text = text.replace(text[i], ' ')

l = text.split()
print(len(l))
l.sort()
for i in l:
    print(i)
