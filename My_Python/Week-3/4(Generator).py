'''
在 Python 中，使用了 yield 的函数被称为生成器（generator）。

跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。

调用一个生成器函数，返回的是一个迭代器对象
'''
# Ex-1:
def f():
    yield 1
    yield 2
    yield 3

print(f())  # <generator object f at 0x0000019C9354BEB0>
# 调用迭代器

it = f()

print(next(it))     # 1
print(next(it))     # 2
print(next(it))     # 3
print(next(it))     # Error : StopIteration

-----------------------------------------------------------------------------------------------------------------------
# Ex-2:
def f():
    for i in range(10):
        yield i

it = f()

for i in it:
    print(i)   # 0 1 2 3 4 5 6 7 8 9

-----------------------------------------------------------------------------------------------------------------------
# Ex-3 :
def f():
    a,b = 0,1
    for i in range(0,n):
        yield a+b
        a,b = a, a+b

it = f(10)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))



