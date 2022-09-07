#                               3. 递归函数 - Recursion
"""
* 什么是递归函数:
    - 如果在一个函数的函数体内调用该函数本身, 这个函数就称为递归函数
* 递归的组成部分:
    - 递归调用与递归终止条件
* 递归的调用过程
    - 每递归调用一次函数, 都会在栈内存分配一个栈帧
    - 每执行完一次函数, 都会释放相应的空间
* 递归的优缺点
    - 缺点: 占用内存多, 效率低下
    - 优点: 思路和代码简单
"""


# Ex-1: Factorial of number

def fac(n, total):
    if n == 1:
        return total
    total *= n
    return fac(n - 1, total)


print(fac(6, 1))  # 720


# -----------------------------

def fac2(n):
    if n == 1:
        return 1
    return n * (fac2(n - 1))


print(fac2(6))  # 720


# ---------------------------------


def fac3(n):
    if n == 1:
        return 1
    else:
        res = n * fac(n - 1)
        return res


print(fac(6))


# -----------------------------------------------------------------------------------------------------------------
#                                       Ex-2: 斐波那契数列 - Fibonacci sequence
# 1 1 2 3 5 8 13 21 34 55
def fib(n):  # 第几个位置的数字
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(6))   # 8




