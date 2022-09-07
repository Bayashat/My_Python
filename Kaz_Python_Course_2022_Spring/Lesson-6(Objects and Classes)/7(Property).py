# Property can only create in __init__ func

class Cats:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def drink(self):
        print(f"{self.name} is drinking")


Cat1 = Cats("Tom")
Cat2 = Cats("Lazy_Cat")

Cat1.eat()  #
Cat2.eat()



