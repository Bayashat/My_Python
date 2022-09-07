from math import *
Answer = 0
a = 1
b = 1

for i in range(10):
    Answer += (a / (b*b))
    b += 1

print(sqrt(Answer*6))