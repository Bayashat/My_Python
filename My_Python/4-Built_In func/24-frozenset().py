##############  24.frozenset()

'''
The frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable).

# Syntax:
frozenset(iterable)

iterable	----    An iterable object, like list, set, tuple etc.

'''

'''
*********************************************************************************************************************
'''

# Ex-1: Freeze the list, and make it unchangeable:

mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)    # frozenset({'banana', 'cherry', 'apple'})


# Ex--2: Try to change the value of a frozenset item.

# This will cause an error:

mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
x[1] = "strawberry" # Error