                  ## 1. Variables that are created outside of a function (as in all of the examples above) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()  # Python is awesome

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.

------------------------------------------------------------------------------------------------------------------------
                  ## 2.The global Keyword
# To create a global variable inside a function, you can use the global keyword.

# If you use the global keyword, the variable belongs to the global scope:
def myfunc2():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

------------------------------------------------------------------------------------------------------------------------

                  ## 3.Also, use the global keyword if you want to change a global variable inside a function.

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc3():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
