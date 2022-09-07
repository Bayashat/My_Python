import math
import platform
from mymodule2 import person1
'''

 What is the Module:
    A file containing a set of functions you want to include in  your application

'''

                ####<1> Create a module:

def greeting(name):
    print("Hello, " + name)
    

            ###### <2> Use a module 
import mymodule
mymodule.greeting("Aibat")


            ##### <3> Variables in Module 
# 1: I saved this code as a file
 # person1 = {"name" : "John", "age" : 36, "country" : "America"}

 # 2. 
import mymodule2

a = mymodule2.person1["age"]
print(a) # 36

# 3.
import mymodule2 as mx
a = mx.person1["name"]
print(a)


            ####### <4> Built-in Modules:


x = platform.system()
print(x)

                ### dir() function : 
x = dir(math)
print(x)

                #  IMport from module:
print(person1["country"])