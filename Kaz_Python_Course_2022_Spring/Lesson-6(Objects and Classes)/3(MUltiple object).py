class Cats:
    def eat(self):
        print("Cat is eating")

    def drink(self):
        print("Cat is drinking")

Tom = Cats()
Tom.eat()
Tom.drink()
print(Tom)   # 

Lazy_Cat = Cats()
Lazy_Cat.eat()
Lazy_Cat.drink()

Lazy_Cat2 = Lazy_Cat
print(Lazy_Cat)
print(Lazy_Cat2)