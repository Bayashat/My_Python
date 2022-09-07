"""                     < 1 > Access Items
"""

#                       1. Indexing

this_list = ["apple", "banana", "cherry"]
print(this_list[1])  # "banana"
# -------------------------------------------------------------------------------

#                       2.Negative Indexing
# Means start from the end.
# -1 refers to the last item, -2 refers to the second last item etc.

this_list = ["apple", "banana", "cherry"]
print(this_list[-1]) # "cherry"
# ------------------------------------------------------------------------------------

#                       3.Range of Indexes-1
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:5])  # "cherry", "orange", "kiwi"
# -----------------------------------------------------------------------------------

#                       4.Range of Indexes-2
# This example returns the items from the beginning to, but NOT including, "kiwi":

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[:4]) # "apple", "banana", "cherry", "orange"
# -------------------------------------------------------------------------------------

#                       5.Range of Indexes-3
# This example returns the items from "cherry" to the end:

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:])  # "cherry", "orange", "kiwi", "melon", "mango"
# ------------------------------------------------------------------------------------

#                       6.Range of Negative Indexes
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[-4:-1])  # "orange", "kiwi", "melon"
# ----------------------------------------------------------------------------------------

#                       7.Check if Item Exists
# Check if "apple" is present in the list:

this_list = ["apple", "banana", "cherry"]
if "apple" in this_list:
  print("Yes, 'apple' is in the fruits list")
# -------------------------------------------------------------------------------------------------

#                       8.与string 不同的是：字符串不能使用下标修改其中的数据， 但是列表可以使用下标修改其中的数据：
l = [1,3.14,True]
l[1] = 'issac'
print(l)  # [1, 'issac', True]