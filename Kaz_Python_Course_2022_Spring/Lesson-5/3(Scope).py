# A variable is only available from inside the refion it is created. THis is called Scope

                # <1> Local Scope
# 1)

from re import X


def my_func():
    x = 300
    print(f"Inside the function {x}")


# print(x)  # Error

# Function inside function:
def my_func2():
    x = 300
    def my_innerfunct():
        print(x)
    my_innerfunct()

my_func2()


                # <2> Global Scope: A variable created in the main body of the Python code is global variable and belongs to the global scope
# 1):
x = 300

def my_func():
    print(x)
my_func()

                # <3> Global keyword:
# 1):
def my_func():
    global x 
    x = 500

my_func()
print(x)