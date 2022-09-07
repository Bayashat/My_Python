"""
                            < 4 > Find & Replace - 查找和替换 方法
1. string.startswith(str)   : 检查字符串是否以str开头,是则返回True
2. string.endswith(str)     : 检查字符串是否以str结束,是则返回True
3. string.find(str, start=0, end=len(string))   : 检测str是否包含在string中, 如果start和end指定范围, 则检查是否包含在指定范围内, 
    如果是返回开始的索引值, 否则返回-1
4. string.rfind(str, start=0, end=len(string))  : 类似于 find() 函数, 不过是从右边开始查找
5. string.index(str, start=0, end=len(string))  : 跟 find() 方法类似, 只不过如果str不在string会报错
6. string.rindex(str, start=0, end=len(string)) : 类似于index(), 不过是从右边开始
7. string.replace(old_str, new_str, num=string.count(old)) : 把string中的old_str替换成new_str, 如果num指定, 则替换不超过num次
"""

hello_str = "hello, hello world"

#                   1. string.startswith(str) : 判断是否以指定字符串开始
print(hello_str.startswith("hello"))  # True
print(hello_str.startswith("Hello"))  # False

# --------------------------------------------------------------------------------------------------------------------
#                   2. string.endswith(str) : 判断是否以指定字符串结束
print(hello_str.startswith("world"))  # True

# --------------------------------------------------------------------------------------------------------------------
#                   3. string.find(str, start=0, end=len(string)) : 查找指定字符串 返回开始的索引值,否则返回-1
# sub_str: 要在字符串中查找的内容，类型str
# start : 开始位置,从哪里开始查找，默认是0
# end : 结束位置,查找到哪里结束,默认是 len()
print(hello_str.find("llo"))  # 2
print(hello_str.find("abc"))  # -1

# -------------------------------------------------------------------------------------------------------------------
#                   4. string.rfind(str, start=0, end=len(string))  : 类似于 find() 函数, 不过是从右边开始查找
print(hello_str.rfind("llo"))  # 9
print(hello_str.rfind("abc"))  # -1

# -------------------------------------------------------------------------------------------------------------------
#                   5. string.index(str, start=0, end=len(string))  : 跟 find() 方法类似, 唯一的区别是: 若没有找到，会报错
#   它也有叫 rindex() 的，也是从右边(后面)开始查找
s = "Hello"
print(s.index("l"))  # 2
print(s.index("x"))  # Error

# ---------------------------------------------------------------------------------------------------------------------
#                   6. string.replace(old_str, new_str, num=string.count(old)) : 替换字符串'
#                          replace方法执行完成后, 会返回一个新的字符串
#                          注意: 不会修改原有字符串的内容

print(hello_str.replace("world", "python"))  # "hello, hello python"
print(hello_str)  # "hello, hello world"

# -------------------------------------------------------------------------------------------------------------------
#                   7.Replace String-2 : 替换字符串
# my_str.replace(old_str, new_str, count)
# old_str: 将要被替换的字符串
# new_str: 新的，替换成的字符串
# count: 替换的次数， 默认 全部替换
# 返回值： 得到一个新的字符串，不会改变原来的字符串

my_str = 'hello world it_cast and it_cast_cpp'
my_str1 = my_str.replace('it_cast', 'it_heima')
print(my_str1)  # "hello world it_heima and it_heima_cpp"

my_str2 = my_str.replace('it_cast', 'it_heima', 1)  # 仅替换一次
print(my_str2)  # "hello world it_heima and it_cast_cpp"
