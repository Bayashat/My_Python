'''
callable(object)	Returns True if the specified object is callable, otherwise False
'''

def hello():
    print("hi")

print(callable(hello))  # True

class Person:
    name = "john"
    age = 20

    def get_age(self):
        return self.age

p = Person()

print(callable(Person))  # True
print(callable(p))  # False
print(callable(p.get_age)) # True