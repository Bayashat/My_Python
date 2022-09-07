 # Private  : 

class Cats:

    def __init__(self):
        self.name = "Tom"
        self.__age = 15

    def eat(self):
        print(f"{self.name} is eating")
    
    def __cats_age(self):
        print(f"cat's age is {self.__age}")

    def drink(self):
        print(f"{self.name} is drinking")


Cat1 = Cats()

print(Cat1.name)
# print(Cat1.__age)

Cat1.__cats_age()

