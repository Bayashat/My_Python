##################          1. The match() function

##  re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。re.match只匹配字符串的开始.
# 函数语法:
re.match(pattern, string, flags=0)

# 函数参数说明：
'''

pattern	    匹配的正则表达式
string	    要匹配的字符串。
flags	    标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志

匹配成功re.match方法返回一个匹配的对象，否则返回None。

我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式:

group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
groups()	    返回一个包含所有小组字符串的元组，从 1 到 所含的小组号


'''
----------------------------------------------------------------------------------------------------------------------------
'''            
                                                #### Ex-1: 
import re
print(re.match('www', 'www.runoob.com').span())  # (0,3)
print(re.match('com', 'www.runoob.com'))         # None

'''
----------------------------------------------------------------------------------------------------------------------------


                                                #### Ex-2:

import re
 
line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if matchObj:
   print ("matchObj.group() : ", matchObj.group())      # Cats are smarter than dogs
   print ("matchObj.group(1) : ", matchObj.group(1))    # Cats
   print ("matchObj.group(2) : ", matchObj.group(2))    # smarter
else:
   print ("No match!!")

