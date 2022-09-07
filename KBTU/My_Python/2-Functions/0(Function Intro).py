"""
                  < 0 > Function Intro
 * 函数就是将一段具有独立功能的代码块 整合到⼀个整体并命名,在需要的位置调用这个名称即可完成对应的需求。

 * 为什么需要函数:
    - 复用代码
    - 隐藏实现细节
    - 提高可维护性
    - 提高可读性便于测试

 * 函数的使用包含两个步骤:
    1. 定义函数 -- 封装独立的功能
    2. 调用函数 -- 享受封装的成果

  * 函数的作用 : 在开发过程中, 使用函数可以提高编写的效率以及代码的重用

  * 定义函数须知:
    1. def 是英文 define 的缩写
    2. 函数名称应该能够表达 函数封装代码的功能, 方便后续的调用
    3. 函数名称 的命名应该符合 标识符的命名规则:
      * 可以由 字母, 数字, 下划线 和 数字 组成
      * 不能以数字开头
      * 不能与关键字重名
"""


#                     1.Creating a Function
def my_function():
    print("Hello from a function")


# -------------------------------------------------------------------------------------------------------------------
#                     2.Calling a Function
# To call a function, use the function name followed by parenthesis:

def my_function():
    print("Hello from a function")


my_function()


# ---------------------------------------------------------------------------------------------------------------------
#                     3.Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.

def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)
'''
apple
banana
cherry
'''


# -----------------------------------------------------------------------------------------------------------------
#                     4.Return Values

def my_function(x):
    return 5 * x


print(my_function(3))  # 15


# -------------------------------------------------------------------------------------------------------------------
#                     5.The pass Statement
#  function definitions cannot be empty, but if you for some reason have a function definition with no content,
#  put in the pass statement to avoid getting an error.

def myfunction():
    pass


# --------------------------------------------------------------------------------------------------------------------
#                     7. 指定参数的数据类型
def my_function(x: int):
    print(x)


my_function(3)  # 3


def my_function2(x: str):
    print(x)


my_function2(3)  # "3"
# ---------------------------------------------------------------------------------------------------------------
#                     8. 函数的说明文档:也就是函数的注释，告诉别人，这个函数是干什么的
"""
def 函数名(参数):
  ''' 说明文档的位置 '''
  代码
  ......
"""


# 查看函数的说明文档:  help(Function name)

# -------------------------------------------------------------------------------------------------------------------
#                       9. returns Many values:
# 一个函数多个返回值的方法:
def return_num():
    return 1, 2  # 返回tuple
    # 在return后面可以直接写 列表， 字典， 返回多个值
    return [100, 200]
    return {'name': 'python', 'age': 20}


result = return_num()
print(result)  # (1, 2)
#   Ex-1:


def fun(num_list):
    odd = []  # 存奇数
    even = []  # 存偶数

    for i in num_list:
        if i % 2:  # if i % 2 != 0
            odd.append(i)
        else:
            even.append(i)
    return odd, even


# 函数的调用
lst = [10, 29, 34, 23, 44, 53, 55]
print(fun(lst))  # ([29, 23, 53, 55], [10, 34, 44])

