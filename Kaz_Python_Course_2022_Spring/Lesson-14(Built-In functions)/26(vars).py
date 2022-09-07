'''
vars(object)	Returns the __dict__ property of an object

'''

class Person:
    name = "john",
    age = 20

x = vars(Person)
print(x)