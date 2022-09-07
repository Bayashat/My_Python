"""
                        < 3 > Remove Set Items
"""
#                    (1) Set.remove() : 删除集合中的指定数据，如果数据不存在则报错
this_set = {10, 20, 30, 40, 50}

this_set.remove(10)
print(this_set) # {20，30，40，50}

this_set.remove(100) # KeyError

# --------------------------------------------------------------------------------------------------------------------
#                       (2) Set.discard() : 删除集合中的指定数据，如果数据不存在也不会报错
this_set = {10,20,30,40,50}

this_set.discard(10)
print(this_set)  # {20,,30,40,50}

this_set.discard(100)
print(this_set) # 20,30,40,50

####  Note: If the item to remove does not exist, discard() will NOT raise an error.
# -------------------------------------------------------------------------------------------------------------------
#                       (3) Set.pop() : 随机删除集合中的某个数据，并返回这个数据.
                #  pop() 方法不能填参数, 填了就会 TypeError
# You can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.

this_set = {10,20,30,40,50}
x = this_set.pop()

print(x)    # 40

print(this_set) # 10,20,30,50
# --------------------------------------------------------------------------------------------------
#                       (4) Set.clear()
# The clear() method empties the set:

this_set = {"apple", "banana", "cherry"}

this_set.clear()

print(this_set)
# --------------------------------------------------------------------------------------------------------
#                       (5) del() Set
# The del keyword will delete the set completely:

this_set = {"apple", "banana", "cherry"}

del this_set

print(this_set)
# -------------------------------------------------------------------------------------------------------

