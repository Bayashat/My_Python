                                ## 1. There are three numeric types in Python:

int
float
complex

x = 1    # int
y = 2.8  # float
z = 1j   # complex always has "j"

# Note: You cannot convert complex numbers into another number type.

# ------------------------------------------------------------------------------------------------------------------------
                                ## 1.1 Float numbers

x = 1.1
y = 2.2
print(x+y)  # 3.3000000000000003

from decimal import Decimal
print(Decimal(x) + Decimal(y))  # 3.3

# ------------------------------------------------------------------------------------------------------------------------
                                ## 2. Random Number
# Import the random module, and display a random number between 1 and 9:

import random

print(random.randrange(1, 10))  # don't contain 10

# ------------------------------------------------------------------------------------------------------------------------
                                    ## 3.Number functions
#  1. abs(x)	     return absolute value: abs(-10) : 10
#  2.ceil(x)	     返回数字的上入整数， : math.ceil(4.1) 返回 5
#  3.cmp(x, y)       如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃，使用 (x>y)-(x<y) 替换。
#  4.exp(x)	         返回e的x次幂(e^x) : math.exp(1) 返回2.718281828459045
#  5.fabs(x)	     返回数字的绝对值， 如math.fabs(-10) 返回10.0
#  6.floor(x)	     返回数字的下舍整数，如math.floor(4.9)返回 4
#  7.log(x)	         如math.log(math.e)返回1.0,math.log(100,10)返回2.0
#  8.log10(x)	     返回以10为基数的x的对数，如math.log10(100)返回 2.0
#  9.max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
#  10.min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
#  11.modf(x)	        返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
#  12.pow(x, y)	        x**y 运算后的值。
#  13.round(x [,n])     返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。 其实准确的说是保留值将保留到离上一位更近的一端。
#  14. sqrt(x)	        返回数字x的平方根。


# ------------------------------------------------------------------------------------------------------------------------
                                ## 5.Trigonometric functions
#  1.acos(x)	   返回x的反余弦弧度值。
#  2.asin(x)	   返回x的反正弦弧度值。
#  3.atan(x)	   返回x的反正切弧度值。
#  4.atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
#  5.cos(x)	        返回x的弧度的余弦值。
#  6.hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
#  7.sin(x)	        返回的x弧度的正弦值。
#  8.tan(x)	        返回x弧度的正切值。
#  9.degrees(x)	    将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
#  10.radians(x)	将角度转换为弧度

# ------------------------------------------------------------------------------------------------------------------------