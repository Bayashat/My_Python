#                         2. Python Lambda
# 使用lambda关键字定义匿名函数.
# A lambda function is a small anonymous function.
# 如果一个函数有⼀个返回值, 并且只有一句代码, 可以使⽤ lambda简化。
# A lambda function can take any number of arguments, but can only have one expression.

#                           (1) Syntax 语法
"""
lambda arguments : expression
lambda 参数列表 : 表达式
"""


# 注意
# lambda表达式的参数可有可无, 函数的参数在lambda表达式中完全适⽤
# lambda函数能接收任何数量的参数但只能返回一个表达式的值
# ---------------------------------------------------------------------------------------------------------------
#                           2.1 Example
# Ex-1 : 用函数
def fun1():
    return 200


print(fun1)  # <function fn1 at 0x000002E8AB62E040>
print(fun1())  # 200

# lambda表达式
fn2 = lambda: 100
print(fn2)  # <function <lambda> at 0x000002E8AB81CC10>
print(fn2())  # 100


# 注意：直接打印lambda表达式，输出的是此lambda的内存地址

# -------------------------------------------------------------------------------------------------------------------
#                           2.2 Example : calculate a+b
# 1) Use function :
def add(a, b):
    return a + b


print(add(2 + 3))  # 5

# 2) Use lambda:
fn = lambda a, b: a + b
print(fn(1, 2))  # 3
# or
print((lambda a, b: a + b)(1, 2))  # 3

# ------------------------------------------------------------------------------------------------------------------
#                           (3) Lambda parameters

#                       3.1 No parameter / 无参数
(lambda: print("hello"))()

fn1 = lambda: 100
print(fn1())  # 100
# or
print((lambda: 100)())  # 100

#                       3.2 With one parameter 1个参数
fn2 = lambda a: a
print(fn2('Hello World'))  # Hello World
# or
print((lambda a: a)("Hello World"))

#                       3.3 default parameter 默认,缺省参数
fn3 = lambda a, b, c=100: a + b + c
print(fn3(10, 20))  # 130

print(fn3(10, 20, 200))  # 230
# or
print((lambda a, b, c=100: a + b + c)(10, 20))  # 130

#                       3.4 可变参数 *args
fn4 = lambda *args: args
print(fn4(1, 2, 3))  # (1,2,3)
# or
print((lambda *args: args)(10, 20, 30))  # (10, 20, 30)

# 注意: 这⾥的可变参数传入到lambda之后, 返回值为元组

#                       3.5 可变参数 **kwargs
fn5 = lambda **kwargs: kwargs
print(fn5(name='Python', age=20))  # {'name':'Python' , 'age' : 20}
# or
print((lambda **kwargs: kwargs)(name='python', age=20))

# ---------------------------------------------------------------------------------------------------------------------
#                           (4) Application of Lambda
#                       4.1 Lambda with judgment 带判断的Lambda
fn1 = lambda a, b: a if a > b else b
print(fn1(1000, 500))
# or
print((lambda a, b: a if a > b else b)(1000, 500))

#                       4.2 列表数据按字典key的值排序
students = [
    {'name': 'c', 'age': 20},
    {'name': 'a', 'age': 19},
    {'name': 'b', 'age': 22}
]

# 直接sort会报错, 因为list里的数据是 dict, 程序不知道怎么sort
students.sort()
print(students)  # Error

#  Sort(key,reverse):
#  Key----形参,需要传递一个函数,指定规则,列表的数据根据什么排序.
#  Reverse=True : 逆序,倒序排序      Reverse=False : 升序排序，可以不写reverse


#   1. 按name值升序排列
students.sort(key=lambda x: x['name'])
print(students)  # [{'name': 'a', 'age': 19}, {'name': 'b', 'age': 22}, {'name': 'c', 'age': 20}]

#   2. 按name值降序排列
students.sort(key=lambda x: x['name'], reverse=True)
print(students)  # [{'name': 'c', 'age': 20}, {'name': 'b', 'age': 22}, {'name': 'a', 'age': 19}]

#   3. 按age值升序排列
students.sort(key=lambda x: x['age'])
print(students)  # [{'name': 'a', 'age': 19}, {'name': 'c', 'age': 20}, {'name': 'b', 'age': 22}]

#                       4.3  Additional example:
#  need sort by length:

list1 = ['bde', 'a', 'gt', 'stag']

# 默认是按照首字母sort
list1.sort()
print(list1)  # ['a', 'bde', 'gt', 'stag']

# 按length sort
list1.sort(key=lambda x: len(x))
print(list1)  # ['a', 'gt', 'bde', 'stag']

# 按length 降序sort
list1.sort(key=lambda x: len(x), reverse=True)
print(list1)  # ['stag', 'bde', 'gt', 'a']

# --------------------------------------------------------------------------------------------------------------------
#                         5. 当第一个排序规则相同, 还可按第二, 第三个规则排序,需要写元组:
# syntax: sort(key=lambda 形参 : (排序规则1，排序规则2....)
students.sort(key=lambda x: (x['age'], x['name']))


# [{'name': 'a', 'age': 19}, {'name': 'c', 'age': 20}, {'name': 'b', 'age': 22}]

# --------------------------------------------------------------------------------------------------------------------
#                         6. Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

#      1. Use that function definition to make a function that always doubles the number you send in:

def myfunc(n):
    return lambda a: a * n


my_doubler = myfunc(2)

print(my_doubler(11))  # 22


#     2. Or, use the same function definition to make both functions, in the same program:

def myfunc(n):
    return lambda a: a * n


my_doubler = myfunc(2)
my_triploid = myfunc(3)

print(my_doubler(11))
print(my_triploid(11))


# ---------------------------------------------------------------------------------------------------------------------
def calc(opr):
    if opr == '+':
        return lambda a, b: (a + b)  # 替代add函数
    else:
        return lambda a, b: (a - b)  # 替代sub函数


f1 = calc('+')
f2 = calc('-')
print("10 + 5 = {0}".format(f1(10, 5)))
print("10 - 5 = {0}".format(f2(10, 5)))
