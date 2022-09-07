                            ### RegEx --- Regular Expression
'''
 RegEx can be used to check if a string contains the specified search pattern.

正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。

re 模块使 Python 语言拥有全部的正则表达式功能。

'''
                            ### 1.RegEx Module
import re

                            ### 2.RegEx in Python
# Search the string to see if it starts with "The" and ends with "Spain":

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)  # <re.Match object; span=(0, 17), match='The rain in Spain'>

'''
----------------------------------------------------------------------------------------------------------------------
'''

                              #####. 3 Using r prefix before RegEx
#  When r or R prefix is used before a regular expression, it means raw string.
     #  For example, '\n' is a new line whereas r'\n' means two characters: a backslash \ followed by n.


import re

string = '\n and \r are escape sequences.'

result = re.findall(r'[\n\r]', string)
print(result)

# Output: ['\n', '\r']

'''
----------------------------------------------------------------------------------------------------------------------
'''

                                   ### 4.RegEx Functions

 # 1.findall	    Returns a list containing all matches
 # 2.search	        Returns a Match object if there is a match anywhere in the string
 # 3.split	        Returns a list where the string has been split at each match
 # 4.sub	        Replaces one or many matches with a string

'''
----------------------------------------------------------------------------------------------------------------------
'''

                              #### 5.正则表达式修饰符 - 可选标志
#  正则表达式可以包含一些可选标志修饰符来控制匹配的模式。修饰符被指定为一个可选的标志。多个标志可以通过按位 OR(|) 它们来指定。如 re.I | re.M 被设置成 I 和 M 标志：
'''

1. re.I	     使匹配对大小写不敏感
               忽略大小写


2. re.L	     做本地化识别（locale-aware）匹配
               表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境


3. re.M	     多行匹配，影响 ^ 和 $
               多行模式


4. re.S	     使 . 匹配包括换行在内的所有字符
               即为 . 并且包括换行符在内的任意字符（. 不包括换行符）


5. re.U	     根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
               表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库

6. re.X	     该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解.
               为了增加可读性，忽略空格和 # 后面的注释


'''