############       6.The sub() Function

#  The sub() function replaces the matches with the text of your choice:
# Python 的re模块提供了re.sub用于替换字符串中的匹配项。

#语法：
re.sub(pattern, repl, string, count=0, flags=0)

# 参数：

pattern :   正则中的模式字符串。
repl :      替换的字符串，也可为一个函数。
string :    要被查找替换的原始字符串。
count :     模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
flags :     编译时用的匹配模式，数字形式.

前三个为必选参数，后两个为可选参数。

'''
-----------------------------------------------------------------------------------------------------------------------------------------
'''


                                    #### Ex-1: Replace every white-space character with the number 9:

import re

txt = "The rain in Spain"

x = re.sub("\s", "9", txt)
print(x)   # The9rain9in9Spain

You can control the number of replacements by specifying the count parameter:


'''
-----------------------------------------------------------------------------------------------------------------------------------------
'''
                                    #### Ex-2: Replace the first 2 occurrences:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)    # The9rain9in Spain

'''
-----------------------------------------------------------------------------------------------------------------------------------------
'''

                                    #### Ex-3 : 若是这种txt, 我们想要替换多空格为一个空格:

txt = "The       rain     in    spain"

x = re.sub("\s+"," " , txt)      #  表示把 \s+ , 也就是有1或多个空格的地方 替换为 " "

print(x)     #  The rain in spain

'''
-----------------------------------------------------------------------------------------------------------------------------------------
'''
                                        #### 4.import re
 
phone = "2004-959-559 # 这是一个电话号码"
 
# 删除注释
num = re.sub(r'#.*$', "", phone)
print ("电话号码 : ", num)      # 电话号码 :  2004-959-559 
 
# 移除非数字的内容
num = re.sub(r'\D', "", phone)  
print ("电话号码 : ", num)      # 电话号码 :  2004959559

'''
----------------------------------------------------------------------------------------------------------------------------------------
'''
                                    #### 5 repl 参数是一个函数
# 以下实例中将字符串中的匹配的数字乘于 2：

import re
 
# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
 
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))  # A46G8HFD1134

