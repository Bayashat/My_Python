"""
                    < 8 > Split & Join - 拆分和连接
1. string.partition(str)    : 把字符串string分成一个3元素的元组(str前面, str, str后面)
2. string.rpartition(str)   : 类似于partition()函数, 不过是从右边开始查找
3. string.split(str="", maxsplit) : 以str为分隔符切片string, 如果maxsplit有指定值, 则仅分隔maxsplit+1个子字符串,
                                    str默认包含'\r', '\t', '\n' 和空格
4. string.rsplit(str="", maxsplit) : 和split类似, 从右边开始

4. string.splitlines()      : 按照行('\r','\n','\r\n')分隔, 返回一个包含各行作为元素的列表
5. string.join(seq) : 以string作为分隔符, 将seq中所有的元素(的字符串表示)合并为一个新的字符串

"""
#               1. string.split(str="", num)  :  拆分字符串
# 以str为分隔符切片string, 如果num有指定值, 则仅分隔num+1个子字符串, str默认包含'\r', '\t', '\n' 和空格

poem_str = "Hi\t what\n are you\n doing up\t whats up"
print(poem_str)

l = poem_str.split()
print(l)  # ['Hi', 'what', 'are', 'you', 'doing', 'up', 'whats', 'up']

# ----------------------------------------------------------------------------------------------------------------------
#               2. string.join(seq) : 合并字符串
# 以string作为分隔符, 将seq中所有的元素(的字符串表示)合并为一个新的字符串
s = " ".join(l)
print(s)  # "Hi what are you doing up whats up"

my_str = '-'.join("hello") # 会把_加入到hello每两个元素之间， 即
print(my_str)  # h_e_l_l_o
print('_*_'.join("hello")) # h_*_e_*_l_*_l_*_o

my_list = ['hello', 'cpp','python']
print('_'.join(my_list))  # hello_cpp_python

# ----------------------------------------------------------------------------------------------------------------------
#               3. string.partition(str) : 把字符串string分成一个3元素的元组(str前面, str, str后面)

txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)    # ('I could eat ', 'bananas', ' all day')

# ----------------------------------------------------------------------------------------------------------------------
#               4. string.rpartition(str)   : 类似于partition()函数, 不过是从右边开始查找

txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")

print(x)    # ('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')

# ----------------------------------------------------------------------------------------------------------------------
#               5. string.splitlines()   : 按照行('\r','\n','\r\n')分隔, 返回一个包含各行作为元素的列表

txt = "Hello\nThank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)    # ['Hello', 'Thank you for the music', 'Welcome to the jungle']


