
                            ### 5. The split() Function
# split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：
# The split() function returns a list where the string has been split at each match:

re.split(pattern, string[, maxsplit=0, flags=0])

# 参数:
1.pattern	    匹配的正则表达式
2.string	    要匹配的字符串。
3.maxsplit	分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
4.flags	    标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志

'''
-------------------------------------------------------------------------------------------------------------------------------------------
'''

                                        #### Ex-1: Split at each white-space character:

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)    # ['The', 'rain', 'in', 'Spain']

# You can control the number of occurrences by specifying the maxsplit parameter:


'''
-------------------------------------------------------------------------------------------------------------------------------------------
'''

                                    #### Ex-2 :Split the string only at the first occurrence:

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)   # ['The', 'rain in Spain']


'''
-------------------------------------------------------------------------------------------------------------------------------------------
'''

                                    #### Ex-3 : 若是这种txt, арасында бостық көп,

txt = "The       rain     in    spain"

x = re.split("\s+",txt)  # \s+ 表示可以有多个空格

print(x)  # ['The', 'rain', 'in', 'spain']


'''
-------------------------------------------------------------------------------------------------------------------------------------------
'''

                                ##### Ex-4:
import re

re.split('\W+', 'runoob, runoob, runoob.')  # ['runoob', 'runoob', 'runoob', '']

 re.split('(\W+)', ' runoob, runoob, runoob.')  # ['', ' ', 'runoob', ', ', 'runoob', ', ', 'runoob', '.', '']

 re.split('\W+', ' runoob, runoob, runoob.', 1) # ['', 'runoob, runoob, runoob.']

 re.split('a*', 'hello world')   # 对于一个找不到匹配的字符串而言，split 不会对其作出分割: ['hello world']
