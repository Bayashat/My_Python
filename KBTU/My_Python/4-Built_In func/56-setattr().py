##########  56.setattr()

'''

The setattr() function sets the value of the specified attribute of the specified object.

# Syntax: 
setattr(object, attribute, value)

object	    ----    Required. An object.
attribute	----    Required. The name of the attribute you want to set
value	    ----    Required. The value you want to give the specified attribute

'''

'''
*********************************************************************************************************************
'''

# Ex-1: Change the value of the "age" property of the "person" object:

class Person:
  name = "John"
  age = 36
  country = "Norway"

setattr(Person, 'age', 40)
