#                       4. 函数类型
"""
* Python 中的任意一个函数都有数据类型, 这种数据类型是 function, 被称为函数类型
*
    - 一个函数可以作为另一个函数返回值使用
    - 一个函数可以作为另一个函数参数使用
"""


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def square(a):
    return a * a


# 定义计算函数:
def calc(opr):
    if opr == '+':
        return add
    else:
        return sub


f1 = calc('+')  # f1 实际上是 add 函数
f2 = calc('-')  # f2 实际上是 sub 函数
print(type(f1))  # <class 'function'>

print("10 + 5 = {0}".format(f1(10, 5)))  # 10 + 5 = 15
print("10 - 5 = {0}".format(f2(10, 5)))  # 10 - 5 = 5
