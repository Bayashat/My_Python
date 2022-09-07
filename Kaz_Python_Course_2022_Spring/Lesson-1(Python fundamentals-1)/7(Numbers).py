#               <1>
'''
int
float
complex
'''
x = 1   # int
y = 2.8 # float
z = 1j  # complex always has 'j'
# You cannot convert complex numbers to another number type

#               <2>  Random number
# display random number from  1 - 9
import random

print(random.randrange(1,10))  # don't contain 10

#           <3> Number functions
#   1. abs(x)    return absolute value
abs(-10)    # 10

#  2. ceil(x)   return the heiger of a number
import math
math.ceil(4.1)  # 5

# 3. floor(x)
math.floor(4.9) # 4

# 4. exp(x)    return the power of e  (e^x)
math.exp(1)    # 2.71828

# 5. log(x)
math.log(100,10)  # 2
math.log(math.e)  # 1.0

# 6. log10(x)
math.log10(100)  # 2

# 7. max(x,y...)

# 8. min(x,y...)

# 9. pow(x,y)   x^y
pow(2,3)   # 8

# 10. sqrt(x)
math.sqrt(16)   # 4

#               <6>    Trigonometric functions
# 1. acos(x)
# 2. asin(x)
# 3. atan(x)
# 4. sin(x)
# 5. cos(x)
# 6. hypot(x,y)
# 7. degrees(x)
degrees(math.pi / 2)   # 90.0
# 8. radian(x)