'''
map()	Returns the specified iterator with the specified function applied to each item

map(function, iterables)
'''
def myfunc(x):
    return len(x)

x = map(myfunc, ('apple', "banana", "cherry"))

print(list(x))  # [5, 6, 6]

## Ex-2
def myfunc2(a,b):
    return a+b

x = map(myfunc2, ('apple', "banana", "cherry"), ("orange", "lemon", "pineapple"))
print(list(x))