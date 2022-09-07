########################     2. The compile() function

## compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
# 语法格式为：
re.compile(pattern[, flags])

''' 
pattern : 一个字符串形式的正则表达式
flags : 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：


'''
----------------------------------------------------------------------------------------------------------------------------------------
'''
                                            ###### Ex-1:
import re
pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
print m     # None

m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
print m     # None

m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
print m      # <_sre.SRE_Match object at 0x10a42aac0>    # 返回一个 Match 对象


m.group(0)   # 可省略 0
'12'
m.start(0)   # 可省略 0
3
m.end(0)     # 可省略 0
5
m.span(0)    # 可省略 0
(3, 5)


在上面，当匹配成功时返回一个 Match 对象，其中：

group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
span([group]) 方法返回 (start(group), end(group))
'''

'''
----------------------------------------------------------------------------------------------------------------------------------------
'''
                                        ####  EX-2:
import re
pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
m = pattern.match('Hello World Wide Web')
print( m )     # <_sre.SRE_Match object at 0x10bea83e8>  # 匹配成功，返回一个 Match 对象

m.group(0)     # 'Hello World'                            # 返回匹配成功的整个子串

m.span(0)      # (0, 11)                                  # 返回匹配成功的整个子串的索引

 m.group(1)    # 'Hello'                                  # 返回第一个分组匹配成功的子串

 m.span(1)     # (0, 5)                                   # 返回第一个分组匹配成功的子串的索引

 m.group(2)    # 'World'                        # 返回第二个分组匹配成功的子串

 m.span(2)     # (6, 11)                        # 返回第二个分组匹配成功的子串索引

 m.groups()    # ('Hello', 'World')                        # 等价于 (m.group(1), m.group(2), ...)

 m.group(3)                            # 不存在第三个分组

Traceback (most recent call last):
File "<stdin>", line 1, in <module>
IndexError: no such group

