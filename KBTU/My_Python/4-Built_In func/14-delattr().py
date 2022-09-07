################   14.delattr()

''''
The delattr() function will delete the specified attribute from the specified object.

# Syntax: 
delattr(object, attribute)

object	    ----    Required. An object.

attribute   ----	  Required. The name of the attribute you want to remove
'''

'''
*********************************************************************************************************************
'''

# Ex-1: Delete the "age" property from the "person" object:

class Person:
  name = "John"
  age = 36
  country = "Norway"

delattr(Person, 'age')