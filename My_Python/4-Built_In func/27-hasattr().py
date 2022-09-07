#############  27.hasattr()

'''
The hasattr() function returns True if the specified object has the specified attribute, otherwise False.

# Syntax: 
hasattr(object, attribute)

object	    ----    Required. An object.
attribute	----    The name of the attribute you want to check if exists

'''

'''
*********************************************************************************************************************
'''

# Ex-1: Check if the "Person" object has the "age" property:

class Person:
  name = "John"
  age = 36
  country = "Norway"

x = hasattr(Person, 'age')
print(x)    # true