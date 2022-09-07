t  = ("apple", "banana", "cherry")
"""
                    < 0 > Tuple Intro
    Tuple(元组)与列表相似, 不同之处在于元组的 "元素不能改(增删改查)"
* 元组 表示多个元素组成的序列
* 用于存储 一串信息, 数据之间使用 "," 分隔
* 用()定义
* 索引从0开始
"""

#               1. tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
this_tuple = ("apple", "banana", "cherry")
print(this_tuple)
# --------------------------------------------------------------------------------------------------------------------
#               2.Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.

# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# --------------------------------------------------------------------------------------------------------------------
#               3.Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

#               4.Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

#               5.Allow Duplicates
# Since tuple are indexed, tuples can have items with the same value:

# -------------------------------------------------------------------------------------------------------------------
#               6.Tuple Length
# use the len() function:

this_tuple = ("apple", "banana", "cherry")
print(len(this_tuple))  # 3

# ------------------------------------------------------------------------------------------------------------------------
#               7.Create Tuple With One Item
# To create a tuple with only one item, you have to add a "comma" after the item

this_tuple = ("apple",)  # 定义一个元组时要加逗号
print(type(this_tuple))

tuple2 = (10, )  # int类型
# --------------------------------------------------------------------------------------------------------------------
#               8.Tuple Items - Data Types

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple can contain different data types:

tuple1 = ("abc", 34, True, 40, "male")
# --------------------------------------------------------------------------------------------------------------------
#               9.type()
# From Python's perspective, tuples are defined as objects with the data type 'tuple':
# <class 'tuple'>

my_tuple = ("apple", "banana", "cherry")
print(type(my_tuple))
# ---------------------------------------------------------------------------------------------------------------------
#               10.The tuple() Constructor
# Using the tuple() method to make a tuple:

this_tuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(this_tuple)
# ----------------------------------------------------------------------------------------------------------------------
#               11.Create empty tuple:
t = tuple()
t2 = ()
