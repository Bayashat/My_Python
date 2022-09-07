################ 65.vars()

'''
The vars() function returns the __dic__ attribute of an object.

The __dict__ attribute is a dictionary containing the object's changeable attributes.

Note: calling the vars() function without parameters will return a dictionary containing the local symbol table.

# Syntax
vars(object)

object	----    Any object with a __dict__attribute

'''

# Ex-1: Return the __dict__ atribute of an object called Person:

class Person:
  name = "John"
  age = 36
  country = "norway"

x = vars(Person)    # {'__module__': '__main__', 'name': 'John', 'age': 36, 'country': 'norway', '__dict__': <attribute '__dict__' of 'Person' objects>,
                        #  '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}

