# Inheritance :   subclass(father_class)
class Animal:
    def eat(self):
        print("is eating")
    def drink(self):
        print("is drinking")
    def run(self):
        print("is running")
    def sleep(self):
        print("is sleeping")

class dog(Animal):
    def Ury(self):
        print("arf, arf")


Aktos = dog()
Aktos.run()
Aktos.Ury()

