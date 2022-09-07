'''
enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object

'''

import enum


x = ("apple", "banana", "cherry")

print(list(enumerate(x)))  # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

for index, val in enumerate(x):
    print(f"{index} -> {val}")