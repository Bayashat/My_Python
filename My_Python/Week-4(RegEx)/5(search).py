                       ### 6 The search() func
# re.search 扫描整个字符串并返回第一个成功的匹配。匹配成功re.search方法返回一个匹配的对象，否则返回None。
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
# 而re.search匹配整个字符串，直到找到一个匹配。

# 函数语法: 
re.search(pattern, string, flags=0)

# 参数:
pattern	        匹配的正则表达式
string	        要匹配的字符串。
flags	        标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志

# 我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。

group(num=0)	    匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
groups()	        返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。

'''
---------------------------------------------------------------------------------------------------------------------------------------------
'''

                                        #### Ex-1: Search for the first white-space character in the string:
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())  #  3


'''
---------------------------------------------------------------------------------------------------------------------------------------------
'''


                                         ##### Ex-2 :
import re

print(re.search('www', 'www.runoob.com').span())    # (0,3)
print(re.search('com', 'www.runoob.com').span())    # （11，14）



'''
---------------------------------------------------------------------------------------------------------------------------------------------
'''


                                         ##### Ex-3:

txt = "The rain in Spain 1234"
x = re.search(r"(.+)([0-9]+)", txt)     # 查2个group, 一个需要是任意字符，一个是0-9的数字. 由于整个都是任意字符，所有留最后的4给第二个group

print(x.group(0))   # The rain in Spain 1234
print(x.group(1))   # The rain in Spain 123
print(x.group(2))   # 4

# 要是想让 1234 在另一个group, 怎么办?1
txt = "The rain in Spain 1234"
x = re.search(r"(.+)(\b[0-9]+)", txt)   # \b 代表边界

print(x.groups())   # ('The rain in Spain ', '1234')


                                           ##### Ex-4 : 还可以将groups 以字符名来使用
txt = "The rain in Spain 1234"
x = re.search(r"(?P<txt>.+)(?P<number>\b[0-9]+)", txt)   # 通过在 group 的前边写: ?P<字符名>便可以使用字符名来调用group

print(x.group("txt")) # The rain in Spain
print(x.group("number"))    # 1234