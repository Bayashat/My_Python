############ 64.type()

'''

The type() function returns the type of the specified object

# Syntax:
type(object, bases, dict)

object	----    Required. If only one parameter is specified, the type() function returns the type of this object
bases	----    Optional. Specifies the base classes
dict	----    Optional. Specifies the namespace with the definition for the class

'''

# Ex-1: Return the type of these objects:

a = ('apple', 'banana', 'cherry')
b = "Hello World"
c = 33

x = type(a)     # tuple
y = type(b)     # str
z = type(c)     # int