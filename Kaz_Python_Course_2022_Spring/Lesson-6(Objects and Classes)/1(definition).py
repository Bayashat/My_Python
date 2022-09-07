'''
 Алдымен клласс, сосын ғана обьект болады

Классты құру кезінде :
1. Class name
2. Property
3. Methods : create it just like functions, and it should has a parametr : self

to create an object :  objecct_name = class_name()

class Cats:
    def eat(self, parameter):
        print("Cat is eating")
    def drink(self, parameter):
        print("Cat is drinking")


Class has 3 built-in functions: 
1. __init__
2. __del__
3. __str__
'''

class Cats:
    def eat(self, food):
        print(f"Cat is eating {food}")

    def drink(self, water):
        print(f"Cat is drinking {water}")

Cat1 = Cats()

Cat1.eat("Fish")
Cat1.drink("milk")

