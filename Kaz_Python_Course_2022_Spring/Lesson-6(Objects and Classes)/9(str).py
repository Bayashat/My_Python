class Cats:

    def eat(self):
        print(f"{self.name} is eating")

    def drink(self):
        print(f"{self.name} is drinking")

    def __str__(self):
        return "It's about cats"

Cat1 = Cats()

print(Cat1)

