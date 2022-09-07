########### 1. standard

def user_info(name, age, id):
    print(f'Your name is {name}, age is {age}, id is {id}')

user_info("Tom", 18, 1745)


##########   2. Keyword arguments 
def user_info(name, age, id):
    print(f'Your name is {name}, age is {age}, id is {id}')

user_info(age=18, name= "Sara", id=7844)


###########  3. Default parametr value

def user_info(name, age, id = 6544):
    print(f'Your name is {name}, age is {age}, id is {id}')

user_info("Tom", 18)

#########   4. Arbitrary arguments : *args
def my_func(*kids):
    print("The youngest child is " + kids[2])

my_func("Emil", "Tom", "Sara")