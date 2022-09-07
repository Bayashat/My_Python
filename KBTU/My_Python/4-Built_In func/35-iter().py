###############   35.iter()

'''
The iter() function returns an iterator object.

# Syntax:
iter(object, sentinel)

object	    ----    Required. An iterable object
sentinel	----    Optional. If the object is a callable object the iteration will stop when the returned value is the same as the sentinel

'''

'''
*********************************************************************************************************************
'''

# Ex-1: Create an iterator object, and print the items:

x = iter(["apple", "banana", "cherry"])
print(next(x))  # apple
print(next(x))  # banana
print(next(x))  # cherry

