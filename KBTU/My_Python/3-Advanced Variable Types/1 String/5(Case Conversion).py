
"""                    < 5 > 大小写转换 - Case Conversion
1. string.capitalize() : 把字符串的第一个字符大写
2. string.title()      : 把字符串的每个单词首字母大写
3. string.lower()      : 转换string中所有大写字符为小写
4. string.upper()      : 转换string中的小写字母为大写
5. string.swapcase()   : 翻转string中的大小写
"""

#                           1. string.capitalize()  : 把字符串的第一个字符大写, 其它的都小写
my_str = 'hello world it_cast and it_cast_cpp'
print(my_str.capitalize())  # Hello world it_cast and it_cast_cpp

print(my_str)  # hello world it_cast and it_cast_cpp

# -------------------------------------------------------------------------------------------------------------------
#                           2. string.title() : 把字符串的每个单词首字母大写
my_str = 'hello world it_cast and it_cast_cpp'
print(my_str.title())  # Hello World It_Cast And It_Cast_Cpp

print(my_str)  # hello world it_cast and it_cast_cpp

# -------------------------------------------------------------------------------------------------------------------
#                           3. string.lower() : 转换string中所有大写字符为小写
my_str = 'HEllo WORLD IT_cast and IT_cast_cpP'
print(my_str.lower())  # "hello world it_cast and it_cast_cpp"
print(my_str)  # "HEllo WORLD IT_cast and IT_cast_cpP"

# -------------------------------------------------------------------------------------------------------------------
#                           4. string.upper() : 转换string中的小写字母为大写
my_str = 'hello world it_cast and it_cast_cpp'
print(my_str.upper())  # HELLO WORLD IT_CAST AND IT_CAST_CPP
print(my_str)  # hello world it_cast and it_cast_cpp

# -------------------------------------------------------------------------------------------------------------------
#                           5. string.swapcase() : 翻转string中的大小写
my_str = 'HEllo WORLD IT_cast and IT_cast_cpP'
print(my_str.swapcase())  # "heLLO world it_CAST AND it_CAST_CPp"
print(my_str)  # 'HEllo WORLD IT_cast and IT_cast_cpP'


# ---------------------------------------------------------------------------------------------------------------------
