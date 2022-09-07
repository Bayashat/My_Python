                                ### 1.Higher-order functions
# 把函数作为参数传⼊，这样的函数称为高阶函数，⾼阶函数是函数式编程的体现。函数式编程就是指这种高度抽象的编程范式
                                ## 1.1 Abs and Round
# 在Python中， abs() 函数可以完成对数字求绝对值计算。
abs(-10) # 10

# round 函数可以完成对数字的四舍五入计算.
round(1.2) # 1
round(1.9) # 2

                                ## 1.2 体验高阶函数
# 需求:按指定要求，对数字进行整理后(绝对值或四舍五入)进行加法运算

# 写法-1
def add_num(a, b):
    return abs(a) + abs(b)

result = add_num(-1, 2)
print(result) # 3


# 写法-2 高阶函数
def sum_num(a, b, f):   # f 是第3个函数,用来接受将来传入的函数
    return f(a) + f(b)

result = sum_num(-1, 2, abs)
print(result) # 3
# 函数式编程大量使用函数，减少了代码的重复，因此程序比较短，开发速度较快
