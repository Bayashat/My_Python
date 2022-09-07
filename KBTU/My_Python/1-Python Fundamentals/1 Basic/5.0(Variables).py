            # 转换数据类型的作⽤

问: input()接收⽤户输入的数据都是字符串类型，如果⽤户输⼊1，想得到整型该如何操作？
答：转换数据类型即可，即将字符串类型转换成整型

x = int(input())
-------------------------------------------------------------------------------------------------------

                    # <1> eval() 还原原来的数据类型，去掉字符串的引号
num1 = eval("100") # int 100
num2 = eval("3.14") # float 3.14

x= 10
# 常见的数据类型转换：

int(x,[base]) # 将x转换为一个整数  （不行 base 的话默认转换为10进制类型）
float(x)      # 将x转换为一个浮点数
complex(real[,image]) # 创建一个复数，real为实部， image 为虚部
str(x)       # 将x转化为字符串
repr(x)      # 将x转换为表达式字符串
eval(str)    # 用来计算在字符串中的有效python表达式，并返回一个对象.
tuple(s)     # 将序列s转换为一个元组
list(s)      # 将序列s转换为一个列表
chr(x)       # 将一个整数转换为一个unicode字符
ord(x)       # 将一个字符转换为它的ASCII整数值
hex(x)       # 将一个整数转化为一个十六进制字符串
oct(x)       # 将一个整数转化为一个八进制字符串
bin(x)       # 将一个整数转化为一个二进制字符串

--------------------------------------------------------------------------------------------------------------