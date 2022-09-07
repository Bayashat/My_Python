#   Once a set is created, you cannot change its items, but you can add new items
"""
                    < 2 > Add set items
"""


#                   (1) Set.add(): 只添加单一数据
this_set = {"apple", "banana", "cherry"}

this_set.add("orange")

print(this_set)

# ------------------------------------------------------------------------------------------------------
#                   (2.1) Set.update(): 增加序列数据, 不支持加单一数据
# To add items from another set into the current set, use the update() method.

this_set = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

this_set.update(tropical)
print(this_set)  # {'apple', 'mango', 'papaya', 'cherry', 'pineapple', 'banana'}

# ----------------------------------------------------------------------------------------------------------
#                   (2.2) Set.update(): Add Any Iterable
this_set = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

this_set.update(mylist)
print(this_set)  # {'banana', 'cherry', 'apple', 'kiwi', 'orange'}


this_set.update([10, 20, 30])

print(this_set)  # {10, 'orange', 'cherry', 'apple', 'banana', 20, 'kiwi', 30}

