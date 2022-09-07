class Cats:
    def __init__(self):  # init function will automatically called when the object has been created
        print("I am from init function")


    def eat(self):
        print(f"{self.name} is eating")

    def drink(self):
        print(f"{self.name} is drinking")


Cat1 = Cats()

