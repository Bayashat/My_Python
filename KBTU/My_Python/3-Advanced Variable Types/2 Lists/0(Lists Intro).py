""""                   < 0 > List Intro
 * Lists are used to store multiple items in a single variable.

* List(列表)是Python中使用 最频繁 的数据类型, 在其它语言中通常叫做 数组(Array)
* 专门用来存储 "一串信息" , 就是使用一个变量, 存储多个数据
* 列表用 [] 来定义, 数据之间使用 , 分隔
* 列表的索引从 0 开始
"""

this_list = ["apple", "banana", "cherry"]
print(this_list)
# ------------------------------------------------------------------------------------------------
#                       1.List Items
# List items are ordered, changeable, and allow duplicate values.

# List items are indexed, the first item has index [0], the second item has index [1] etc.
# -------------------------------------------------------------------------------------------------
#                       2.List Length
this_list = ["apple", "banana", "cherry"]
print(len(this_list))  # 3
# ----------------------------------------------------------------------------------------------------
#                       3.List Items - Data Types
# List items can be of any data type:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]
# --------------------------------------------------------------------------------------------------
#                       4.The list() Constructor
# Using the list() constructor to make a List:

this_list = list(("apple", "banana", "cherry")) # note the double round-brackets
print(this_list)
# ------------------------------------------------------------------------------------------------------
#                       5.Create empty list:
L = list()

my_list = []

