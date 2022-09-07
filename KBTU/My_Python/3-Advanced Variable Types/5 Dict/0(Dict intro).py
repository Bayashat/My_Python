"""
                      < 0 > Dict Intro
"""
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
"""
      * 字典(dict)是 除列表以外 最灵活的数据类型
      * 字典同样可以用来 存储多个数据
        - 通常用于存储 描述一个"物体"的相关信息
      * 和列表的区别:
        - 列表是 "有序" 的对象集合
        - 字典是 "无序" 的对象集合 : 当输出时,顺序会不一样
      * 字典用 {} 定义
      * 字典使用 键值对 存储数据, 键值对之间用 ',' 分隔
        - '键'(key) 是索引
        - '值'(value)是数据
        - '键'和'值'之间使用 : 分隔  
        - '键'必须是唯一的
        - '值'可以取任何数据类型, 但'键'只能使用 '字符串','数字'或'元组'
"""
# -------------------------------------------------------------------------------------------------------
#                         1.Dictionary
# Dictionaries are used to store data values in "key:value" pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(this_dict)
# -------------------------------------------------------------------------------------------------------------------
#                         2.Dictionary Items
# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in "key:value" pairs, and can be referred to by using the key name.

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(this_dict["brand"]) # "Ford"
# --------------------------------------------------------------------------------------------------------------------
#                       3.Ordered or Unordered?
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.
# --------------------------------------------------------------------------------------------------------------------
#                       4.Changeable
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# -------------------------------------------------------------------------------------------------------------------
#                       5.Duplicates Not Allowed
# Dionaries cannot have two items with the same key:
# -----------------------------------------------------------------------------------------------------------------
#                       6.Dictionary Length
# use # the len() function:

print(len(this_dict))  # 3
# ------------------------------------------------------------------------------------------------------------------
#                       7.dictionary Items - Data Types
# values in dictionary items can be of any data type:

this_dict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
# ----------------------------------------------------------------------------------------------------------------
#                       8.type()
# From Python's perspective, dictionaries are defined as objects with the data type 'dict':

# <class 'dict'>

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(this_dict))
# ----------------------------------------------------------------------------------------------------------------
#                       9.Create empty dict:
d = {}
d = dict()

d = dict(zip([102, 105, 109], ["Jack", "Tom", "William"]))  # {102:"Jack", 105:"Tom", 109:"William"}


