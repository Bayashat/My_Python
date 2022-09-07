###############  9.callable()
'''
The callable() function returns True if the specified object is callable, otherwise it returns False.
'''
# Syntax
callable(object)
# object ---- The object you want to test if it is callable or not.

'''
*********************************************************************************************************************
'''

def hello():
  print('hi')

print(callable(hello))  # True

class Person:
  name = 'Person 1'
  age = 20

  def get_age(self): # instance method
    return self.age

p = Person()

print(callable(Person))  #True
print(callable(p))  # False
print(callable(p.get_age))  # True

