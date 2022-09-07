#   Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

                                ###   <1> Built-in Math Functions
1) The min() and max() functions can be used to find the lowest or highest value in an iterable:
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)    # 5
print(y)    # 25

2) The abs() function returns the absolute (positive) value of the specified number:
x = abs(-7.25)

print(x) # 7.25

3) The pow(x, y) function returns the value of x to the power of y (xy).
Return the value of 4 to the power of 3 (same as 4 * 4 * 4):

x = pow(4, 3)

print(x)    # 64

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
                                    #   <2> The Math Module
Python has also a built-in module called math, which extends the list of mathematical functions.
To use it, you must import the math module:

import math

When you have imported the math module, you can start using methods and constants of the module.

1) The math.sqrt() method for example, returns the square root of a number:

import math

x = math.sqrt(64)
print(x)    # 8

2) The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, 
    and returns the result:

Example
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

3) The math.pi constant, returns the value of PI (3.14...):

import math

x = math.pi

print(x)    # 3.141592653589793
--------------------------------------------------------------------------------------------------------------------------------------
                                ### <3> Math Methods
# math.acos()	        Returns the arc cosine of a number
# math.acosh()	        Returns the inverse hyperbolic cosine of a number
# math.asin()	        Returns the arc sine of a number
# math.asinh()	        Returns the inverse hyperbolic sine of a number
# math.atan()	        Returns the arc tangent of a number in radians
# math.atan2()	        Returns the arc tangent of y/x in radians
# math.atanh()	        Returns the inverse hyperbolic tangent of a number
# math.ceil()	        Rounds a number up to the nearest integer
# math.comb()	        Returns the number of ways to choose k items from n items without repetition and order
# math.copysign()	    Returns a float consisting of the value of the first parameter and the sign of the second parameter
# math.cos()	        Returns the cosine of a number
# math.cosh()	        Returns the hyperbolic cosine of a number
# math.degrees()	    Converts an angle from radians to degrees
# math.dist()	        Returns the Euclidean distance between two points (p and q), where p and q are the coordinates of that point
# math.erf()	        Returns the error function of a number
# math.erfc()	        Returns the complementary error function of a number
# math.exp()	        Returns E raised to the power of x
# math.expm1()	        Returns Ex - 1
# math.fabs()	        Returns the absolute value of a number
# math.factorial()	    Returns the factorial of a number
# math.floor()	        Rounds a number down to the nearest integer
# math.fmod()	        Returns the remainder of x/y
# math.frexp()	        Returns the mantissa and the exponent, of a specified number
# math.fsum()	        Returns the sum of all items in any iterable (tuples, arrays, lists, etc.)
# math.gamma()	        Returns the gamma function at x
# math.gcd()	        Returns the greatest common divisor of two integers
# math.hypot()	        Returns the Euclidean norm
# math.isclose()	    Checks whether two values are close to each other, or not
# math.isfinite()	    Checks whether a number is finite or not
# math.isinf()	        Checks whether a number is infinite or not
# math.isnan()	        Checks whether a value is NaN (not a number) or not
# math.isqrt()	        Rounds a square root number downwards to the nearest integer
# math.ldexp()	        Returns the inverse of math.frexp() which is x * (2**i) of the given numbers x and i
# math.lgamma()	        Returns the log gamma value of x
# math.log()	        Returns the natural logarithm of a number, or the logarithm of number to base
# math.log10()	        Returns the base-10 logarithm of x
# math.log1p()	        Returns the natural logarithm of 1+x
# math.log2()	        Returns the base-2 logarithm of x
# math.perm()	        Returns the number of ways to choose k items from n items with order and without repetition
# math.pow()	        Returns the value of x to the power of y
# math.prod()	        Returns the product of all the elements in an iterable
# math.radians()	    Converts a degree value into radians
# math.remainder()	    Returns the closest value that can make numerator completely divisible by the denominator
# math.sin()	        Returns the sine of a number
# math.sinh()	        Returns the hyperbolic sine of a number
# math.sqrt()	        Returns the square root of a number
# math.tan()	        Returns the tangent of a number
# math.tanh()	        Returns the hyperbolic tangent of a number
# math.trunc()	        Returns the truncated integer parts of a number

------------------------------------------------------------------------------------------------------------------------
                                ### <4> Math Constants
# math.e	   Returns Euler's number (2.7182...)
# math.inf	   Returns a floating-point positive infinity
# math.nan	   Returns a floating-point NaN (Not a Number) value
# math.pi	   Returns PI (3.1415...)
# math.tau	   Returns tau (6.2831...)

----------------------------------------------------------------------------------------------------------------------
                                ### 5.Number functions
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

-----------------------------------------------------------------------------------------------------------------------
                                 ## 6.Random functions:
#  1.choice(seq)	 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
#  2.randrange ([start,] stop [,step])	        从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
#  3.random()	          随机生成下一个实数，它在[0,1)范围内。
#  4.seed([x])	          改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
#  5.shuffle(lst)	      将序列的所有元素随机排序
#  6.uniform(x, y)	      随机生成下一个实数，它在[x,y]范围内。

------------------------------------------------------------------------------------------------------------------------
                                ## 7.Trigonometric functions
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
