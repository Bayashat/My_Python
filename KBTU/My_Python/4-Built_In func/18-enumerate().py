############   18.enumerate()

'''

The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.

The enumerate() function adds a counter as the key of the enumerate object.

# Syntax
enumerate(iterable, start)

iterable	----    An iterable object
start	    ----    A Number. Defining the start number of the enumerate object. Default 0

'''
def my_enumerate(iterable, start=0):
  n = start
  for item in iterable:
    yield n, item
    n += 1

print(list(my_enumerate(l)))

'''
*********************************************************************************************************************
'''

# Ex-1: Convert a tuple into an enumerate object:

x = ('apple', 'banana', 'cherry')

print(list(enumerate(x)))           # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
print(list(enumerate(x,start=1)))   # [(1, 'apple'), (2, 'banana'), (3, 'cherry')]

for index, val in enumerate(l,1):
    print(f'{index} -> {val}')

'''
1 -> apple
2 -> banana
3 -> cherry
'''