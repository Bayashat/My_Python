'''
delattr(object)	Deletes the specified attribute (property or method) from the specified object

# Syntax:
delattr(object, attribute)

'''

class Person:
    name = "john"
    age = 20
    country = "Almaty"
p = Person()
print(p.age)
delattr(Person, 'age')

# print(p.age)  error
