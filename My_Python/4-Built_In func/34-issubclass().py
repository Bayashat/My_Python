##############  34.issubclass()

'''
The issubclass() function returns True if the specified object is a subclass of the specified object, otherwise False.

# Syntax:
issubclass(object, subclass)

object	    ----    Required. An object.
subclass	----    A class object, or a tuple of class objects

'''

'''
*********************************************************************************************************************
'''

# Ex-1: Check if the class myObj is a subclass of myAge:

class myAge:
  age = 36

class myObj(myAge):
  name = "John"
  age = myAge.age

x = issubclass(myObj, myAge)