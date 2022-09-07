###########  25.getattr()

'''
The getattr() function returns the value of the specified attribute from the specified object.

# Syntax:
getattr(object, attribute, default)

object	    ----    Required. An object.
attribute	----    The name of the attribute you want to get the value from
default	    ----    Optional. The value to return if the attribute does not exist

'''


'''
*********************************************************************************************************************
'''

# Ex-1: Get the value of the "age" property of the "Person" object:

class Person:
  name = "John"
  age = 36
  country = "Norway"

x = getattr(Person, 'age')
print(x)    # 36

# Ex-2: Use the "default" parameter to write a message when the attribute does not exist:

class Person:
  name = "John"
  age = 36
  country = "Norway"

x = getattr(Person, 'page', 'my message')
print(x)    # my message