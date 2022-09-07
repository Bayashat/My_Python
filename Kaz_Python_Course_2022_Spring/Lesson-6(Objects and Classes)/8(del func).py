from tkinter.dnd import DndHandler


class Cats:

    def eat(self):
        print(f"{self.name} is eating")

    def drink(self):
        print(f"{self.name} is drinking")

    def __del__(self):
        print("I am is going")


Cat1 = Cats()
Cat1.name = "TOM"

Cat1.eat()  # 
Cat1.drink()

del Cat1
print("-" * 50)



