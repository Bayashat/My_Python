## 1.Strings - 字符串
"""
* 字符串 
  - 就是 一串字符, 是编程语言中表示文本的数据类型
  - 在Python中字符串是基本类型, 是一个不可变的字符类型
* 使用 " 或 ' 定义
  - 虽然可以使用 "/" 或 '\' 做字符串的转义,但是在实际开发中:
    + 如果字符串内部需要使用 ", 可以使用 ' 定义字符串
    + 如果字符串内部需要使用 ', 可以使用 " 定义字符串
* 可以使用索引获取一个字符串中指定位置的字符, 索引计数从0开始
* 也可以使用 for 循环遍历 字符串中每一个字符
"""
# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' = "hello".
# ----------------------------------------------------------------------------------------------------------
#                           1.Assign String to a Variable

a = "Hello"
print(a)
# ---------------------------------------------------------------------------------------------------------------
#                           2.Multiline Strings - 多行字符串
# You can assign a multiline string to a variable by using 3 quotes . Or three single quotes:'''
b = """Lorem ipsum dolor sit amet,
consecrate disciplining elit,
sed do usermod tempor incident
ut labor et color magna aliquot."""
print(b)
# -------------------------------------------------------------------
#                           3.Strings are Arrays - 字符串是数组
# Get the character at position 1 (remember that the first character has the position 0): 获取第一位置的字符.
a = "Hello, World!"
print(a[1])
# ------------------------------------------------------------------
#                           4.Looping through a String - 遍历字符串
# Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "banana":  # 遍历 banana
    print(x)  # b a n a n a
# --------------------------------------------------------------------------------------------------------------------
#                           5.String Length
# To get the length of a string, use the len() function.
# The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))  # 12
# ---------------------------------------------------------------------------------------------------------------------
#                           7.Check String
# To check if a certain phrase or character is present in a string, we can use the keyword "in".
# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)  # True
# --------------------------------------------------------------------------------------------------------------------
#                           8.Use it in an "if statement":
# print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("Yes, 'expensive' is NOT present.")
