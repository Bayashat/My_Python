#                       1.1 Function 参数

#                       (1) 函数调用的参数传递

#                       1.1  位置实参 Position arguments
#   根据形参对应的位置进行实参传递
#   传递和定义参数的顺序及个数必须一致
#   Arguments are often shortened to "args" in Python documentations.
def calc(a, b):
    c = a + b
    return c


result = calc(10, 20)
print(result)  # 3


# ---------------------------------------------------------------------------------------------------------------------
#                       1.2 Keyword Arguments  关键字实参
#   根据形参名称进行实参传递
#   函数调用, 通过“键=值”形式加以指定. 可以让函数更加清晰, 容易使用, 同时也清除了参数的顺序需求。
#   You can also send arguments with the key = value syntax. This way the order of the arguments does not matter.

def calc(a, b, c):
    d = a + b + c
    return d


result = calc(b=10, c=24, a=15)
print(result)  # 49

# 注意: 函数调用时，如果有位置参数时，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序.
calc(111, c=222, b=333)  #


# The phrase Keyword Arguments are often shortened to "kwargs" in Python documentations.

# -------------------------------------------------------------------------------------------------------------------
#                       1.3 将序列中的每个元素都转换为位置实参
#                            使用 *
def fun(a, b, c):
    print(a, b, c)


fun(10, 20, 30)  # 函数调用时的参数传递, 称为位置传参
lst = [10, 20, 30]
# fun(lst)
fun(*lst)  # 在函数调用时, 将列表中的每个元素都转换为位置实参传入


# -------------------------------------------------------------------------------------------------------------------
#                       1.4 将字典中的每个键值对都转换为关键字实参
#                            使用 **
def fun(a, b, c):
    print(a, b, c)


fun(a=100, b=200, c=300)  # 函数的调用, 所以是关键字实参
dic = {'a': 111, 'b': 222, 'c': 333}
# fun(dic)
fun(**dic)  # 在函数调用时, 将字典中的键值对都转换为关键字实参传入


# ------------------------------------------------------------------------------------------------------------------
#                       (2) 函数定义的参数传递

#                       2.1 Default Parameter Value  缺省参数 / 默认参数
#  缺省参数也叫默认参数, ⽤于定义函数, 为参数提供默认值, 调用函数时可不传该默认参数的值
#  调用函数时, 缺省参数的值如果没有传入, 则取默认值.
#  注意: 所有位置参数必须出现在默认参数前, 包括函数定义和调⽤
#  If we call the function without argument, it uses the default value:

def fun(a, b=10):  # 默认参数
    print(b, a)


def user_info(name, age, gender='男'):
    print(f'您的名字是{name}, 年龄是{age}, 性别是{gender}')


user_info('TOM', 20)  # 您的名字是TOM, 年龄是20, 性别是男
user_info('Rose', 18, '⼥')  # 您的名字是Rose, 年龄是18, 性别是⼥


def make_coffee(name="Cappuccino"):
    return "Make a {0} coffee.".format(name)


print(make_coffee())  # Make a Cappuccino coffee.
print(make_coffee("Latte"))  # Make a Latte coffee.


# ---------------------------------------------------------------------------------------------------------------
#                       2.2 个数可变的位置形参/*args : Arbitrary Arguments(Non-Keyword Arguments) 不定长参数之包裹位置传递
# * 不定长参数也叫可变参数. ⽤于不确定调用的时候会传递多少个参数(不传参也可以)的场景。此时，可用包裹(packing)位置参数，或者包裹关键字参数
#       来进行参数传递，会显得⾮常⽅便
# * 包裹位置传递 : 接受所有位置参数，返回一个"元组"
# If the number of arguments is unknown, add a * before the parameter name:

# Ex-1:
def fun(*args):
    print(args)


fun(100)  # (100,)
fun(100, 200)  # (100, 200)
fun(100, 200, 300)  # (100, 200, 300)


# Ex-2:
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")  # The youngest child is Linus

# 注意：函数调用时，如果为缺省参数传值则修改默认参数值；否则使用这个默认值

# ------------------------------------------------------------------------------------------------------------------
#                       2.3 **kwargs (Keyword Arguments) - 个数可变的关键字形参
"""
1. 定义函数时, 可能无法事先确定传递的关键字实参的个数时, 使用可变的关键字形参
2. 使用 ** 定义个数可变的关键字形参
3. 结果为一个字典
"""


def fun(**kwargs):
    print(kwargs)


fun(a=10)  # {'a': 10}
fun(a=10, b=20, c=30)  # {'a': 10, 'b': 20, 'c': 30}

# 在一个函数的定义过程中, 既有个数可变的关键字形参, 也有个数可变的位置形参 的话, 要求: *args 要放在 **kwargs 之前
"""
def fun2(**arg1, *arg2): 
    pass
"""


def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Jim")


def user_info(**kwargs):
    print(kwargs)


user_info()  # {}  返回了空字典
user_info(name='TOM(')  # {'name': 'TOM'}
user_info(name='TOM', age=18, id=110)  # {'name': 'TOM', 'age': 18, 'id': 110}


# ------------------------------------------------------------------------------------------------------------------------
#                           小总结
# 在形参前边加上一个 * , 该形参变为不定长元组形参，可以接受所有的位置实参, 类型是元组.
# 在形参前边加上两个 ** , 该形参变为不定长字典形参，可以接受所有的关键字实参, 类型是字典.

def func(*args, **kwargs):
    print(args)
    print(kwargs)


func(1, 2, 3, 4, 5)  # (1, 2, 3, 4, 5) {}
func(a=1, b=2, c=3, d=4)  # () {'a': 1, 'b': 2, 'c': 3, 'd': 4}
func(1, 2, 3, a=4, b=5, c=6)  # (1, 2, 3) {'a': 4, 'b': 5, 'c': 6}


# ---------------------------------------------------------------------------------------------------------------
#                           (3)函数形参的完整格式
#  普通形参(a)   缺省形参(b)   不定长元组形参(*args)   不定长字典形参(**kwargs)

#   (1)
def func(a, b=1):  # 先普通，再缺省
    pass


def func1(a, b=1, *args):  # 语法没有错误，但是缺省参数不能使用默认值
    print('a', a)
    print('b', b)
    print(args)


func1(1, 2, 3, 4)  # a 1   b 2    (3,4)


#   (2)
def func2(a, *args, b=1):  # 普通形参，不定长元组形参  缺省形参
    print('a', a)
    print('b', b)
    print(args)


func2(1, 2, 3, 4)  # a 1    b 1    (2,3,4)
func2(1, 2, 3, 4, b=10)  # a 1    b 10    (2,3,4)


#   (3)
def func3(a, *args, b=1, **kwargs):  # 普通形参，不定长元组形参  缺省形参  不定长字典形参
    print('a', a)
    print('b', b)
    print(args)
    print(kwargs)


func3(1, 2, 3, c=4, d=5)  # a 1, b 1, (2, 3), {'c': 4, 'd': 5}
