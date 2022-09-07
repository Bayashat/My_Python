"""
                < 3 > Add Dict Items
"""

#                 (1) Adding Items
# 字典中,使用key值进行添加和修改
# dict[key] = value   : 若key存在，就是修改. 不存在则是添加
# 注意 : key值的 int 1 和 float 1.0 是一样的
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

this_dict = {"brand": "Ford",
             "model": "Mustang",
             "year": 1964,
             "color": "red"}

print(this_dict)
# --------------------------------------------------------------------------------------------------------------
#                 (2) Dict.update({key:value}) : 可合并另一个字典
# The update() method will update the dictionary with the items from a given argument. If the item does not exist,
#     the item will be added.

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict.update({"color": "red"})

