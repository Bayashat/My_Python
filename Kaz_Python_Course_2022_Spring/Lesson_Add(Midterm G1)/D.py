text = input()

d = dict()
l = []
while text:
    l.append(text)
    text = input()

s = set(l)
for i in s:
    num = l.count(i)
    d[i] = num

items = sorted(d.items())


for i in items:  # (str, int)
    if i[1] %2 == 0:
        print(i[0])


