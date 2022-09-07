"""
                            2. 字符串的切片 - Slice string
                                str(start : end : step)
* "切片"方法适用于 "字符串, 列表, 元组"
* 切片 使用 "索引值" 来限定范围, 从一个大的 字符串 中 切出 小的字符串
* 列表 和 元组 都是 有序的集合, 都能够 通过索引值 获取到对应的数据
* 字典是一个 无序的集合, 是使用 键值对 保存数据

"""
#                           1. Slicing - 提取字符串

# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])   # ll0
# --------------------------------------------------------------------------------------------------------
#                           2.Slice From the Start
# Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])  # Hello
# ----------------------------------------------------------------------------------------------------------------
#                           3.Slice To the End
# Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])  # llo, World!
# ----------------------------------------------------------------------------------------------------------
#                           4.Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])  # orl

# -----------------------------------------------------------------------------------------------
#                           5.字符串快速逆置 : String fast inversion
s = 'hello'
print(s[::-1])  # olleh
# -----------------------------------------------------------------------------------------------
#                           6.得到和原来一样的字符串: Get the same Str
a = s[:]
print(a)  # hello