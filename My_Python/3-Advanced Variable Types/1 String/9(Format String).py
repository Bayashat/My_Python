"""
                        < 9 >  Format String - 格式化字符串
    * 1. 使用 % 作占位符
        - %s       : 字符串
        - %i 或 %d : 整数
        - %f       : 浮点数
        例子: "我的名字叫: %s, 今年 %d 岁了" % (name, age)

    * 2. {} 作占位符
        - "我的名字叫: {0}, 今年 {1} 岁了".format(name, age)

    * 3. f-string
        - print(f"My name is {name}, I am {age} years old")
"""

#                           1. 使用 % 作占位符

name = "Bayashat"
age = 19
score = 98.15451
print("My name is %s, I am %d years old, I've got %.3f" % (name, age, score))  # My name is Bayashat, I am 19 years old,
#                                                                                                    I've got 98.155

# -------------------------------------------------------------------------------------------------------------------

#                           2. {} 作占位符

#                           2.1 String format()
#           The format() method allows you to format selected parts of a string.
#           如果只写 ".3" : 代表共3位数, 若是 ".3f" : 则代表小数点后3位


#  (1). Add a placeholder where you want to display the price:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))    # The price is 49 dollars

#  (2). Format the price to be displayed as a number with two decimals:
txt = "The price is {:.2f} dollars"
print(txt.format(price))  # The price is 49.00 dollars

# --------------------------------------------------------------------------------------------------------------------

#                           2.2 Multiple Values
#           If you want to use more values, just add more values to the format() method:
#  And add more placeholders:

quantity = 3
item_num = 567
price = 49
my_order = "I want {} pieces of item number {} for {:.2f} dollars."
print(my_order.format(quantity, item_num, price))  # I want 3 pieces of item number 567 for 49.00 dollars.

# ------------------------------------------------------------------------------------------------------------------
#                           2.3 Index Numbers
# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the
#   correct placeholders:

quantity = 3
item_num = 567
price = 49
my_order = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(my_order.format(quantity, item_num, price))  # I want 3 pieces of item number 567 for 49.00 dollars.

# ------------------------------------------------------------------------------------------------------------------
#                           2.4. Named Indexes
#       You can also use named indexes by entering a name inside the curly brackets {car_name},
#  but then you must use names when you pass the parameter values txt.format(car_name = "Ford"):

my_order = "I have a {car_name}, it is a {model}."
print(my_order.format(car_name="Ford", model="Mustang"))  # I have a Ford, it is a Mustang.

# ------------------------------------------------------------------------------------------------------------------
#                           3. F-String
print(f"My name is {name}, I am {age} years old")  # My name is Bayashat, I am 19 years old
