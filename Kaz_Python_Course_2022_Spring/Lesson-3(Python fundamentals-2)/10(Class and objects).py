'''
Phones class: 
Samsung - object: property, method

'''
############  1. Create a class:
class Phones():
    name = ""
    price = 0

    def Call(self):
        print("calling")

#############  2. Create object

Samsung = Phones()
Samsung.price = 120000
Samsung.Call() # calling

##############  3.
phone1 = Phones()
phone1.price = 2000000
phone1.name = "Samsung"

print(phone1.price) # 2000000







    