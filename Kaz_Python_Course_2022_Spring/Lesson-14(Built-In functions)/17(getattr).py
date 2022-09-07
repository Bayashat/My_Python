'''
getattr()	Returns the value of the specified attribute (property or method)

getattr(object, attribute, default)
'''

class Person:
    name = 'John',
    age = 20

print(getattr(Person, 'age'))  # 20
print(getattr(Person, "country", "Ok"))  # Ok