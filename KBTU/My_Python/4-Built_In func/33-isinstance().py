####################  33.isinstance()

'''
The isinstance() function returns True if the specified object is of the specified type, otherwise False.

If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.

# Syntax: 
isinstance(object, type)

object	----    Required. An object.
type	----    A type or a class, or a tuple of types and/or classes

'''

'''
*********************************************************************************************************************
'''

# Ex-1: Check if the number 5 is an integer:

x = isinstance(5, int)  # True

# Ex-2: Check if "Hello" is one of the types described in the type parameter:

x = isinstance("Hello", (float, int, str, list, dict, tuple))   # True

# Ex-3: Check if y is an instance of myObj:

class myObj:
  name = "John"

y = myObj()

x = isinstance(y, myObj)    # True

