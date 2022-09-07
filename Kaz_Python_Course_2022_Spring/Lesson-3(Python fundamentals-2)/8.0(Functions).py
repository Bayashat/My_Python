  ##########3 1. Creating a func
from re import L


def func_name():
    print("Hello from a function")

  #########  2. Calling a func
func_name()

#######    3. passing a list as an argument to a func

fruits = ['Apple', "banana", "cherry"]
def my_func(food):
    for x in food:
        print(x)

my_func(fruits)

########     4. return values
def my_func(x):
    return 5*x
print(my_func(10)) # 50

########    5.Recursion

