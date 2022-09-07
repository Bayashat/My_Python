####################  43.next()

'''

The next() function returns the next item in an iterator.

You can add a default return value, to return if the iterable has reached to its end.

# Syntax: 

iterable	----    Required. An iterable object.
default	    ----    Optional. An default value to return if the iterable has reached to its end.

'''

'''
*********************************************************************************************************************
'''

# Ex-1: Create an iterator, and print the items one by one:

mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x)    # apple
x = next(mylist)
print(x)    # banana
x = next(mylist)
print(x)    # cherry


# Ex-2: Return a default value when the iterable has reached to its end:

mylist = iter(["apple", "banana", "cherry"])
x = next(mylist, "orange")
print(x)    # apple
x = next(mylist, "orange")
print(x)    # banana
x = next(mylist, "orange")
print(x)    # Bcherry
x = next(mylist, "orange")
print(x)    # orange

