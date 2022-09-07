Answer = 0
a = 4
b = 1

for i in range(10):
    Answer += (a / b)
    a *= -1
    b += 2

print(Answer)