class Cats:

    def eat(self):
        print(f"{self.name} is eating")

    def drink(self):
        print(f"{self.name} is drinking")


Cat1 = Cats()

Cat1.eat()  # 
Cat1.drink()

Cat1.name = "Tom"

