my_set = {"apple", "banana", "cherry"}

"""               
                < 0 > Set intro
    A set is a collection which is both unordered and unindexed.
* 1. 集合中的数据必须是不可变类型
* 2. 集合是可变类型
* 3. 集合是无序的,不支持下标
* 4. 有去重功能
"""
set1 = {[1,2]}  # 会报错，集合中必须是不可变类型

set2 = {"apple", "banana", "cherry"}
# --------------------------------------------------------------------------------------------------------------------
# Note: Sets are unordered, so you cannot be sure in which order the items will appear. 里面的数据会随机排列
# ------------------------------------------------------------------------------------------------
#                       1. Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.
# --------------------------------------------------------------------------------------------------------------------
#                       2. Unordered     无序性
# Unordered means that the items in a set do not have a defined order.
# ------------------------------------------------------------------------------------------------------------------
#      3. Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# --------------------------------------------------------------------------------------------------------------------
#                       4.Unchangeable  确定性
# Sets are unchangeable, meaning that we cannot change the items after the set has been created.

# Once a set is created, you cannot change its items, but you can add new items.
# ----------------------------------------------------------------------------------------------------------------
#                       5.Duplicates Not Allowed    唯一性
# Sets cannot have two items with the same value.

# Duplicate values will be ignored:

this_set = {"apple", "banana", "cherry", "apple"}

print(this_set)  # {'banana', 'apple', 'cherry'}
# ----------------------------------------------------------------------------------------------------------------------
#                       6.Length of a Set

this_set = {"apple", "banana", "cherry"}

print(len(this_set))  # 3
# ------------------------------------------------------------------------------------------------------------------------
#                       7.Set Items - Data Types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = set(range(10))   # {0,1,2,3,4,5,6,7,8,9}
set5 = set('Python')    # {'n', 'h', 'p', 'y', 't', 'o'}
# ---------------------------------------------------------------------------------------------------------------------------
#                       8.A set can contain different data types:

set1 = {"abc", 34, True, 40, "male"}
# -----------------------------------------------------------------------------------------------------------------------------
#                       9.type()
# From Python's perspective, sets are defined as objects with the data type 'set':
# <class 'set'>

my_set = {"apple", "banana", "cherry"}
print(type(my_set))
# ----------------------------------------------------------------------------------------------------------------------------
#                       10.The set() Constructor

this_set = set(("apple", "banana", "cherry")) # note the double round-brackets
print(this_set)
# ------------------------------------------------------------------------------------------------------------------------------
# 12.Construct empty set:
s = set()